import sys
import time
import os
import uuid
from absl import app
from absl import flags
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, TimeoutException

from common.captcha.benchmark.BenchmarkAdditionSolver import CaptchaSolver
from common.pii import Pii
import utils.ScraperUtils as ScraperUtils
from utils.ScraperUtils import Record, Charge, RecordBuilder, ChargeBuilder

FLAGS = flags.FLAGS
flags.DEFINE_string('portal_base', 'https://court.baycoclerk.com/BenchmarkWeb2/', 'Base of the portal to scrape.')
flags.DEFINE_string('state', 'FL', 'State code we are scraping.', short_name='s')
flags.DEFINE_string('county', 'Bay', 'County we are scraping.', short_name='c')

flags.DEFINE_integer('start_year', 2000, 'Year at which to start scraping.', short_name='y')
flags.DEFINE_integer('end_year', datetime.now().year, 'Year at which to end scraping', short_name='e')

flags.DEFINE_bool('solve_captchas', False, 'Whether to solve captchas.')
flags.DEFINE_enum('save_attachments', 'none', ['none', 'filing', 'all'], 'Which attachments to save.', short_name='a')
flags.DEFINE_string('output', 'bay-county-scraped.csv', 'Relative filename for our CSV', short_name='o')

flags.DEFINE_integer('missing_thresh', 5, 'Number of consecutive missing records after which we move to the next year', short_name='t')
flags.DEFINE_integer('connect_thresh', 10, 'Number of failed connection attempts allowed before giving up')

 # TODO(mcsaucy): move everything over to absl.logging so we get this for free
flags.DEFINE_bool('verbose', False, 'Whether to be noisy.')

output_attachments = os.path.join(os.getcwd(), 'attachments')
output_captchas = os.path.join(os.getcwd(), 'captcha')

ffx_profile = webdriver.FirefoxOptions()
# Automatically dismiss unexpected alerts.
ffx_profile.set_capability('unexpectedAlertBehaviour', 'dismiss')

if os.getenv('DOCKERIZED') == 'true':
    # If running through docker-compose, use the standalone firefox container. See: docker-compose.yml#firefox
    driver = webdriver.Remote(
       command_executor='http://firefox:4444/wd/hub',
       desired_capabilities=ffx_profile.to_capabilities())
else:
    driver = webdriver.Firefox(options=ffx_profile)

captcha_solver = CaptchaSolver(out_dir=output_captchas)


def main(argv):
    del argv
    begin_scrape()


def begin_scrape():
    """
    Starts the scraping process. Continues from the last scraped record if the scraper was stopped before.
    :return:
    """
    global driver

    # Find the progress of any past scraping runs to continue from then
    try:
        last_case_number = ScraperUtils.get_last_csv_row(FLAGS.output).split(',')[3]
        print("Continuing from last scrape (Case number: {})".format(last_case_number))
        last_year = 2000 + int(str(last_case_number)[:2])  # I know there's faster ways of doing this. It only runs once ;)
        if not last_case_number.isnumeric():
            last_case_number = last_case_number[:-4]
        last_case = int(str(last_case_number)[-6:])
        FLAGS.end_year = last_year
        continuing = True
    except FileNotFoundError:
        # No existing scraping CSV
        continuing = False
        pass

    # Scrape from the most recent year to the oldest.
    for year in range(FLAGS.end_year, FLAGS.start_year, -1):
        if continuing:
            N = last_case + 1
        else:
            N = 1

        print("Scraping year {} from case {}".format(year, N))
        YY = year % 100

        record_missing_count = 0
        # Increment case numbers until the threshold missing cases is met, then advance to the next year.
        while record_missing_count < FLAGS.missing_thresh:
            # Generate the case number to scrape
            case_number = f'{YY:02}' + f'{N:06}'

            search_result = search_portal(case_number)
            if search_result:
                record_missing_count = 0
                # if multiple associated cases are found,
                # scrape all of them
                if len(search_result) > 1:
                    for case in search_result:
                        search_portal(case)
                        scrape_record(case)
                # only a single case, no multiple associated cases found
                else:
                    scrape_record(case_number)
            else:
                record_missing_count += 1

            N += 1

        continuing = False

        print("Scraping for year {} is complete".format(year))


def scrape_record(case_number):
    """
    Scrapes a record once the case has been opened.
    :param case_number: The current case's case number.
    """
    # Wait for court summary to load
    for i in range(FLAGS.connect_thresh):
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryAccordion')))
        except TimeoutException:
            if i == FLAGS.connect_thresh - 1:
                raise RuntimeError('Summary details did not load for case {}.'.format(case_number))
            else:
                driver.refresh()

    # Get relevant page content
    summary_table_col1 = driver.find_elements_by_xpath('//*[@id="summaryAccordionCollapse"]/table/tbody/tr/td[1]/dl/dd')
    summary_table_col2 = driver.find_elements_by_xpath('//*[@id="summaryAccordionCollapse"]/table/tbody/tr/td[2]/dl/dd')
    summary_table_col3 = driver.find_elements_by_xpath('//*[@id="summaryAccordionCollapse"]/table/tbody/tr/td[3]/dl/dd')

    # Wait for court dockets to load
    for i in range(FLAGS.connect_thresh):
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'gridDocketsView')))
        except TimeoutException:
            if i == FLAGS.connect_thresh - 1:
                raise RuntimeError('Dockets did not load for case {}.'.format(case_number))
            else:
                driver.refresh()

    charges_table = driver.find_elements_by_xpath('//*[@id="gridCharges"]/tbody/tr')
    docket_public_defender = driver.find_elements_by_xpath(
        "//*[contains(text(), 'COURT APPOINTED ATTORNEY') and contains(text(), 'ASSIGNED')]")
    docket_attorney = driver.find_elements_by_xpath("//*[contains(text(), 'DEFENSE') and contains(text(), 'ASSIGNED')]")
    docket_pleas = driver.find_elements_by_xpath("//*[contains(text(), 'PLEA OF')]")
    docket_attachments = driver.find_elements_by_class_name('casedocketimage')

    r = RecordBuilder()
    r.id = str(uuid.uuid4())
    r.state = FLAGS.state
    r.county = FLAGS.county
    r.portal_id = case_number
    r.case_num = Pii.String(summary_table_col2[1].text.strip())
    r.agency_report_num = summary_table_col1[4].text.strip()
    r.arrest_date = None  # Can't be found on this portal
    r.filing_date = summary_table_col1[2].text.strip()
    r.offense_date = None  # Can't be found on this portal
    r.division_name = summary_table_col3[3].text.strip()
    r.case_status = summary_table_col3[1].text.strip()

    # Create list of assigned defense attorney(s)
    defense_attorney_text = list(map(lambda x: x.text, docket_attorney))
    r.defense_attorney = ScraperUtils.parse_attorneys(
            defense_attorney_text)
    # Create list of assigned public defenders / appointed attorneys
    public_defender_text = list(map(lambda x: x.text, docket_public_defender))
    r.public_defender = ScraperUtils.parse_attorneys(
            public_defender_text)
    # Get Judge
    r.judge = Pii.String(summary_table_col1[0].text.strip())

    # Download docket attachments.
    # Todo(OscarVanL): This could be parallelized to speed up scraping if save-attachments is set to 'all'.
    if FLAGS.save_attachments:
        for attachment_link in docket_attachments:
            attachment_text = attachment_link.find_element_by_xpath('./../../td[3]').text.strip()
            if FLAGS.save_attachments == 'filing':
                if not ('CITATION FILED' in attachment_text or 'CASE FILED' in attachment_text):
                    # Attachment is not a filing, don't download it.
                    continue
            ScraperUtils.save_attached_pdf(driver, output_attachments, '{}-{}'.format(case_number, attachment_text),
                                           FLAGS.portal_base, attachment_link, 20, FLAGS.verbose)

    Charges = {}
    for charge in charges_table:
        charge_builder = ChargeBuilder()
        charge_cols = charge.find_elements_by_tag_name('td')
        count = int(charge_cols[0].text.strip())
        charge_builder.count = count

        charge_desc = charge_cols[1].text
        charge_builder.description, charge_builder.statute = (
                ScraperUtils.parse_charge_statute(charge_desc))
        charge_builder.level = charge_cols[2].text.strip()
        charge_builder.degree = charge_cols[3].text.strip()
        # plea = charge_cols[4].text.strip() # Plea is not filled out on this portal.
        charge_builder.disposition = charge_cols[5].text.strip()
        charge_builder.disposition_date = charge_cols[6].text.strip()
        Charges[count] = charge_builder.build()
    r.charges = list(Charges.values())

    # Pleas are not in the 'plea' field, but instead in the dockets.
    for plea_element in docket_pleas:
        plea_text = plea_element.text.strip()
        plea = ScraperUtils.parse_plea_type(plea_text)
        plea_date = plea_element.find_element_by_xpath('./../td[2]').text.strip()
        plea_number = ScraperUtils.parse_plea_case_numbers(plea_text, list(Charges.keys()))

        # If no case number is specified in the plea, then we assume it applies to all charges in the trial.
        if len(plea_number) == 0:
            for charge in Charges.values():
                charge.plea = plea
                charge.plea_date = plea_date
        else:
            # Apply plea to relevant charge count(s).
            for count in plea_number:
                Charges[count].plea = plea
                Charges[count].plea_date = plea_date

    r.arresting_officer = None  # Can't be found on this portal
    r.arresting_officer_badge_number = None  # Can't be found on this portal

    profile_link = driver.find_element_by_xpath("//table[@id='gridParties']/tbody/tr/*[contains(text(), 'DEFENDANT')]/../td[2]/div/a").get_attribute(
       'href')
    # profile_link = driver.find_element_by_xpath('//*[@id="gridParties"]/tbody/tr[1]/td[2]/div[1]/a').get_attribute(
    #     'href')
    load_page(profile_link, 'Party Details:', FLAGS.verbose)

    r.suffix = None
    r.dob = None  # This portal has DOB as N/A for every defendent
    r.race = driver.find_element_by_xpath(
        '//*[@id="fd-table-2"]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[7]/td[2]').text.strip()
    r.sex = driver.find_element_by_xpath(
        '//*[@id="mainTableContent"]/tbody/tr/td/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[6]/td[2]').text.strip()

    # Navigate to party profile
    full_name = driver.find_element_by_xpath(
        '//*[@id="mainTableContent"]/tbody/tr/td/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[2]').text.strip()
    r.middle_name = None
    r.last_name = None
    if ',' in full_name:
        r.first_name, r.middle_name, r.last_name = ScraperUtils.parse_name(full_name)
    else:
        # If there's no comma, it's a corporation name.
        r.first_name = Pii.String(full_name)
    r.party_id = driver.find_element_by_xpath(
        '//*[@id="mainTableContent"]/tbody/tr/td/table/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[8]/td[2]').text.strip()  # PartyID is a field within the portal system to uniquely identify defendants

    record = r.build()
    ScraperUtils.write_csv(FLAGS.output, record, FLAGS.verbose)


def search_portal(case_number):
    """
    Performs a search of the portal from its home page, including selecting the case number input, solving the captcha
    and pressing Search. Also handles the captcha being solved incorrectly
    :param case_number: Case to search
    :return: A set of case number(s).
    """
    # Load portal search page
    load_page(f"{FLAGS.portal_base}/Home.aspx/Search", 'Search', FLAGS.verbose)
    # Give some time for the captcha to load, as it does not load instantly.
    time.sleep(0.8)

    # Select Case Number textbox and enter case number
    select_case_input()
    case_input = driver.find_element_by_id('caseNumber')
    case_input.click()
    case_input.send_keys(case_number)

    # Solve captcha if it is required
    solved_captcha = None
    try:
        # Get Captcha. This is kinda nasty, but if there's no Captcha, then
        # this will throw (which is a good thing in this case) and we can
        # move on with processing.
        captcha_image_elem = driver.find_element_by_xpath('//*/img[@alt="Captcha"]')
        captcha_buffer = captcha_image_elem.screenshot_as_png
        if FLAGS.solve_captchas:
            solved_captcha = captcha_solver.solve_captcha(captcha_buffer)
            captcha_textbox = driver.find_element_by_xpath('//*/input[@name="captcha"]')
            captcha_textbox.click()
            captcha_textbox.send_keys(solved_captcha.answer)

            # Do search
            search_button = driver.find_element_by_id('searchButton')
            search_button.click()
        else:
            print(f"Captcha encountered trying to view case ID {case_number}.")
            print("Please solve the captcha and click the search button to proceed.")
            while True:
                try:
                    WebDriverWait(driver, 6 * 60 * 60).until(
                        lambda x: case_number in driver.title )
                    print("continuing...")
                    break
                except TimeoutException:
                    print("still waiting for user to solve the captcha...")

    except NoSuchElementException:
        # No captcha on the page, continue.
        # Do search
        search_button = driver.find_element_by_id('searchButton')
        search_button.click()

    # If the title stays as 'Search': Captcha solving failed
    # If the title contains the case number or 'Search Results': Captcha solving succeeded
    # If a timeout occurs, retry 'connect_thresh' times.
    for i in range(FLAGS.connect_thresh):
        try:
            # Wait for page to load
            WebDriverWait(driver, 5).until(
                lambda x: 'Search' in driver.title or case_number in driver.title or 'Search Results:' in driver.title)
            # Page loaded
            if driver.title == 'Search':
                # Clicking search did not change the page. This could be because of a failed captcha attempt.
                try:
                    # Check if 'Invalid Captcha' dialog is showing
                    driver.find_element_by_xpath(
                        '//div[@class="alert alert-error"]')
                    print("Captcha was solved incorrectly")

                    if FLAGS.solve_captchas and solved_captcha:
                        solved_captcha.save_captcha(correct=False)
                except NoSuchElementException:
                    pass
                # Clear cookies so a new captcha is presented upon refresh
                driver.delete_all_cookies()
                # Try solving the captcha again.
                search_portal(case_number)
            elif 'Search Results: CaseNumber:' in driver.title:
                # Captcha solved correctly
                if FLAGS.solve_captchas and solved_captcha:
                    solved_captcha.save_captcha(correct=True)
                # Figure out the number of cases returned
                case_count = ScraperUtils.get_search_case_count(driver, FLAGS.county)
                # Case number search found multiple cases.
                if case_count > 1:
                    return ScraperUtils.get_associated_cases(driver)
                # Case number search found no cases
                else:
                    return set()
            elif case_number in driver.title:
                # Captcha solved correctly
                if FLAGS.solve_captchas and solved_captcha:
                    solved_captcha.save_captcha(correct=True)
                # Case number search did find a single court case.
                return {case_number}
        except TimeoutException:
            if i == FLAGS.connect_thresh - 1:
                raise RuntimeError('Case page could not be loaded after {} attempts, or unexpected page title: {}'.format(FLAGS.connect_thresh, driver.title))
            else:
                search_portal(case_number)


def select_case_input():
    """
    Selects the Case Number input on the Case Search window.
    """
    # Wait for case selector to load
    for i in range(FLAGS.connect_thresh):
        try:
            WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, 'title'), 'Case Search'))
        except TimeoutException:
            if i == FLAGS.connect_thresh - 1:
                raise RuntimeError('Portal homepage could not be loaded')
            else:
                load_page(f"{FLAGS.portal_base}/Home.aspx/Search", 'Search', FLAGS.verbose)

    case_selector = driver.find_element_by_xpath(
        '//*/input[@searchtype="CaseNumber"]')
    case_selector.click()
    try:
        case_input = driver.find_element_by_id('caseNumber')
        case_input.click()
    except ElementNotInteractableException:
        # Sometimes the caseNumber box does not appear, this is resolved by clicking to another radio button and back.
        name_selector = driver.find_element_by_xpath(
            '//*/input[@searchtype="Name"]')
        name_selector.cick()
        case_selector.click()
        case_input = driver.find_element_by_id('caseNumber')
        case_input.click()

    return case_input


def load_page(url, expectedTitle, verbose=False):
    """
    Loads a page, but tolerates intermittent connection failures up to 'connect-thresh' times.
    :param url: URL to load
    :param expectedTitle: Part of expected page title if page loads successfully. Either str or list[str].
    """
    if verbose:
        print('Loading page:', url)
    driver.get(url)
    for i in range(FLAGS.connect_thresh):
        try:
            if isinstance(expectedTitle, str):
                WebDriverWait(driver, 5).until(EC.title_contains(expectedTitle))
                return
            elif isinstance(expectedTitle, list):
                WebDriverWait(driver, 5).until(any(x in driver.title for x in expectedTitle))
                return
            else:
                raise ValueError('Unexpected type passed to load_page. Allowed types are str, list[str]')
        except TimeoutException:
            if i == FLAGS.connect_thresh - 1:
                raise RuntimeError('Page {} could not be loaded after {} attempts. Check connction.'.format(url, FLAGS.connect_thresh))
            else:
                if verbose:
                    print('Retrying page (attempt {}/{}): {}'.format(i+1, FLAGS.connect_thresh, url))
                driver.get(url)

    print('Page {} could not be loaded after {} attempts. Check connection.'.format(url, FLAGS.connect_thresh),
          file=sys.stderr)


if __name__ == '__main__':
    if not os.path.exists(output_attachments):
        os.makedirs(output_attachments)
    app.run(main)
