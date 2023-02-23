from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import random
import uuid
import requests
import re
import pandas as pd
import time


class SF_Court_Scraper:
    """
    Scraper class for SF Court data
    """

    dates_to_scrape = []
    session_id = ""
    # Random seed used for rand num generator wait time values
    random_seed = None
    incr = 0

    def __init__(self, date=None, date_range=None, rand_seed=None):
        """
        date or date_range can be entered.

        date: datetime.date("YYYY-MM-DD")
        date_range: tuple of two datetime.date values (start, end)
        rand_seed: Can be set for debugging random wait times if necessary

        Example date_range: ("2021-01-01", "2021-02-01")
        """
        self.sf_court_entry_link = r"https://webapps.sftc.org/captcha/captcha.dll?referrer=https://webapps.sftc.org/ci/CaseInfo.dll?"

        # This is the link that we want to update with the new session ID once we get it after completing the CAPTCHA
        self.session_id = ""
        # Selenium timeout param in seconds. If this is too low we won't be able to complete the CAPTCHA before it times out.
        # A "wait" function could potentially be used instead of timeout; the timeout is nice because it will kill our driver if the CAPTCHA isn't completed.
        self.CAPTCHA_timeout = 30

        # If date_range is passed as a param, then we need to generate a list of date values between the start and end date passed
        # We also want to have a check in place to see whether a single date was also passed. If this is the case, we'll use the single date value instead of the range and provide log output.
        if date_range and not date:
            if date_range[0] > date_range[1]:
                print(
                    "Start Date entered must be less than End Date in 'date_range' param"
                )
                raise ValueError
            # Calculate all of the dates that we want to scrape from the SF Court portal, excluding weekends
            # This is a bit funky. We're getting the difference between the start and end date, adding one to get all of the dates in the range (inclusive)
            num_days_scraping_period = (
                datetime.strptime(date_range[1], "%Y-%m-%d")
                - datetime.strptime(date_range[0], "%Y-%m-%d")
            ).days + 1
            # Use pandas to generate a list of dates based off of our specified range
            temp = pd.bdate_range(date_range[0], periods=num_days_scraping_period)
            # Format the dates : YYYY-MM-DD expected by SF court portal
            self.dates_to_scrape = temp.format(
                formatter=lambda x: x.strftime("%Y-%m-%d")
            )

        elif date:
            self.dates_to_scrape.append(date)

        # Can be used for debugging is necessary
        if rand_seed:
            self.random_seed = rand_seed
        else:
            self.random_seed = uuid.uuid4()

    def _generate_session_id(self):
        """
        Function that gets us a Session ID that can be used with Requests to scrape the San Francisco Court website
        """
        driver = webdriver.Firefox()
        driver.get(self.sf_court_entry_link)
        timeout = self.CAPTCHA_timeout

        # Test whether the user has successfully solved the CAPTCHA.
        # To save SF Court's site resources, we'll close the connection after 30 seconds.
        try:
            element_present = EC.presence_of_element_located((By.ID, "tabs-1"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load and/or user to complete CAPTCHA")
            driver.close()
            return

        # Sample URL after accessing CAPTCHA :  'https://webapps.sftc.org/ci/CaseInfo.dll?&SessionID=50E1755E0EC222BCB0D689F4BE119593447B1F89'
        # We want to get the SessionID param at the end of this url, so we use a bit of regex
        self.session_id = (
            re.search("=.*$", driver.current_url).group(0).replace("=", "")
        )
        print("URL after CAPTCHA:" + driver.current_url)
        print("SessionID value:" + self.session_id)
        print(
            "CAPTCHA Completed! Session ID generated for scraping. Closing Selenium browser session."
        )

        # End condition with driver, close browser
        if driver.window_handles:
            driver.close()

        return

    def _get_record_by_date(self, date_to_scrape):
        """
        This is the method that uses GET requests to call the SF court website once we've obtained a session token/id (stored at class level)

        date : For each specific set of records/GET request, we need a date provided (sample : date="2022-01-01")
        """

        if self.session_id == "":
            self._generate_session_id()

        url = r"https://webapps.sftc.org/ci/CaseInfo.dll/datasnap/rest/TServerMethods1/GetCasesWithFilings/{}/{}".format(
            date_to_scrape, self.session_id
        )
        print("SCRAPING WITH URL : {}".format(url))

        try:
            get_records = requests.get(url)
            if get_records.status_code == 200:
                # TODO : How do we want to route requests response? Use parse_response to grab the requested fields.
                print(get_records.content)
        # In the event of an HTTP error, regenerate a new session ID and restart from last date scraped.
        except requests.exceptions.HTTPError:
            self._generate_session_id()
        # Catch all other exceptions ("nuclear" error code.)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return

    def _wait(self, debug=False):
        """
        Our "wait" function that we'll use to slow down/disguise traffic from the application. We don't want to pull all the records at once (DDOS is bad.) and we also don't want our IP to get flagged/blocked.
        Our easiest way around low-level security after the CAPTCHA is just to use randomized numbers for our wait period between requests.
        """
        random.seed(self.random_seed)
        if self.incr % 3 == 0:
            delay = random.randint(4, 10) + random.uniform(0.0, 1.0)
        if debug:
            print("WAIT DELAY:" + str(delay))
        time.sleep(delay)

    # TODO : Dummy method
    def parse_response(self):
        """
        For each response that we receive from our GET request, we need to parse them with REGEX to extract the required fields
        """
        return


def main():
    temp = SF_Court_Scraper()
    temp._wait(debug=True)
    # temp._get_record_by_date("2022-01-01")
    # temp._get_record_by_date("2023-02-02")
    # temp.get_record_by_date(date_to_scrape="2022-01-01")
    # temp = SF_Court_Scraper(date_range=("2023-01-01", "2022-01-20"))
    # print(temp.dates_to_scrape)


if __name__ == "__main__":
    main()
