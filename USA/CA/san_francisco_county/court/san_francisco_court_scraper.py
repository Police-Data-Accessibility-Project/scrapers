from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import json
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
    # incr used by _wait randomizer, logs
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

        date_specific_url = r"https://webapps.sftc.org/ci/CaseInfo.dll/datasnap/rest/TServerMethods1/GetCasesWithFilings/{}/{}".format(
            date_to_scrape, self.session_id
        )

        print("SCRAPING WITH URL : {}".format(date_specific_url))

        try:
            req = requests.get(date_specific_url)
            if req.status_code == 200:
                # Successful GET request! We will return the response to be parsed.
                return {"date": date_to_scrape, "content": req.content}
        # In the event of an HTTP error, regenerate a new session ID and restart from last date scraped.
        except requests.exceptions.HTTPError:
            self._generate_session_id()
        # Catch all other exceptions ("nuclear" error code.)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def _wait(self, debug=False):
        """
        Our "wait" function that we'll use to slow down/disguise traffic from the application. We don't want to pull all the records at once (DDOS is bad.) and we also don't want our IP to get flagged/blocked.
        Our easiest way around low-level security after the CAPTCHA is just to use randomized numbers for our wait period between requests.
        """
        random.seed(self.random_seed)
        if self.incr % 5 == 0:
            # "long" wait happens every fifth request
            delay = random.randint(10, 15) + random.uniform(0.0, 1.0)
        else:
            delay = random.randint(2, 8) + random.uniform(0.0, 1.0)
        if debug:
            print("WAIT DELAY:" + str(delay))
        time.sleep(delay)

    # TODO : If tests are requested for this, it'd be easy to mock this with a dummy payload that's maintained alongside the code/tests
    
    # TODO : We need to add a case that checks whether or not there exists records. There are some dates which don't have records (example : weekends)
    #        - The response received in this case will still be 200, problem is that the JSON won't have a body to be accessed beyond the string of something like "No Records..."
    #        - This should be easy to implement : Write a REGEX to check for the "no records" indicator, generate a field that has the date with some indicator that there are no records
    def _parse_response(self, response_date, response_json):
        """
        For each response that we receive from our GET request, we need to parse them with REGEX to extract the CASE_NAME and CASE_NUMBER
        Expects a JSON Response payload to parse, date value that is output by _get_record_by_date is used in the final output to track the specific date attached to case name and number

        BE AWARE : This method is fragile. The JSON parser is dependent on how the SF Court webapp stores data. This may need improvement/modification in the future if the SF data format changes for whatever reason.

        returns a DataFrame containing the following columns : DATE, CASE_NUMBER, CASE_TITLE
        """
        raw_response = json.loads(response_json)["result"][1]
        regex_to_extract_case_number = r"[A-Z]{3}-\d*-\d*</A>"
        # List of tuples that we'll use to populate our DataFrame output
        parsed_data = []

        for i in json.loads(raw_response):
            case_number = re.search(regex_to_extract_case_number, str(i))[0].replace(
                "</A>", ""
            )
            case_title = i["CASE_TITLE"]
            parsed_data.append((response_date, case_number, case_title))

        df = pd.DataFrame(parsed_data, columns=["DATE", "CASE_NUMBER", "CASE_TITLE"])

        return df
    
    # TODO : Create a public "get_records" function that handles _wait, multiple date values, checks if the response is none


def main():
    temp = SF_Court_Scraper()
    rat = temp._get_record_by_date("2023-02-25")
    print(
        temp._parse_response(
            response_date=rat["date"], response_json=rat["content"]
        ).head()
    )
    # temp._get_record_by_date("2022-01-01")
    # temp._get_record_by_date("2023-02-02")
    # temp.get_record_by_date(date_to_scrape="2022-01-01")
    # temp = SF_Court_Scraper(date_range=("2023-01-01", "2022-01-20"))
    # print(temp.dates_to_scrape)


if __name__ == "__main__":
    main()
