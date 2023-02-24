from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import json
import random
import uuid
import requests
import re
import pandas as pd
import time

# Hiding deprecation warning for uuid import.
# TODO : This is a sloppy solution. The uuid is just used to generate random numbers in the scrapers _wait() function. Easy item to fix.
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


# TODO : This is a "weak" implementation that doesn't check the user's input dates to see if they're valid.
def get_user_input_dates():
    """
    Helper function to get user input for SF_Court_Scraper class to use.
    """
    print(
        "P.D.A.P. San Francisco Court Scraper.\n---------------\nUSE WITH DISCRETION. This system is intended for data discovery and may not be used as a sole source of truth for legal reference/documentation.\n---------------\nEnter both the START_DATE and END_DATE values in 'YYYY-MM-DD' format (example : 2022-01-03)\n"
    )
    start_date = input("Enter START_DATE : ")
    end_date = input("Enter END_DATE : ")
    return [start_date, end_date]


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
        self.CAPTCHA_timeout = 60

        # If date_range is passed as a param, then we need to generate a list of date values between the start and end date passed
        # We also want to have a check in place to see whether a single date was also passed. If this is the case, we'll use the single date value instead of the range and provide log output.
        if date_range and not date:
            if date_range[0] > date_range[1]:
                print(
                    "Start Date entered must be less than End Date in 'date_range' param"
                )
                raise ValueError
            # Use pandas to generate a list of dates based off of our specified range
            temp = pd.bdate_range(start=date_range[0], end=date_range[1])
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
                # Successful GET request! Next we'll check the content. If it contains string '"result":[-1,""]', we need to regenerate our session token and try again
                if '"result":[-1,""]' in str(req.content):
                    print(
                        "The GET request has indicated that we need to regenerate our session id. Please solve the new CAPTCHA."
                    )
                    self._generate_session_id()
                    pass
                # Content does not contain indicator of failed request, return the records from this get request
                else:
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
    def _parse_response(self, response_date, response_json):
        """
        For each response that we receive from our GET request, we need to parse them with REGEX to extract the CASE_NAME and CASE_NUMBER
        Expects a JSON Response payload to parse, date value that is output by _get_record_by_date is used in the final output to track the specific date attached to case name and number

        BE AWARE : This method is fragile. The JSON parser is dependent on how the SF Court webapp stores data. This may need improvement/modification in the future if the SF data format changes for whatever reason.

        returns a DataFrame containing the following columns : DATE, CASE_NUMBER, CASE_TITLE
        """
        # Edge-case in the event that no cases were found for this specific date (weekend slipped in, date was from the future).
        if "No cases found with filings" in str(response_json):
            print("No cases found for {}".format(response_date))
            return pd.DataFrame(
                [(response_date, "None", "NO CASES FOUND FOR THIS DATE")],
                columns=["DATE", "CASE_NUMBER", "CASE_TITLE"],
            )

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

    def get_records(self):
        dates = []
        if self.dates_to_scrape:
            dates = self.dates_to_scrape
        else:
            dates.append(str(datetime.today("%y-%m-%d")))
        if not os.path.exists("./data"):
            os.makedirs("./data")

        # If the file already exists, don't use a header
        if os.path.exists("./data/sf_court_records.csv"):
            use_header = False
        else:
            use_header = True

        for i in dates:
            print("Scraping record for: ", i)
            temp = self._get_record_by_date(i)
            output = self._parse_response(temp["date"], temp["content"])
            # Output the DataFrame to csv file to persist storage of records outside of scraper runtime
            output.to_csv(
                "data/sf_court_records.csv", mode="a", index=False, header=use_header
            )

            if use_header:
                use_header = False
            # Store the date that we just scraped in dates file
            with open("./data/dates_scraped.txt", "a") as f:
                f.write(i + "\n")
            self._wait()
        print("Scraping complete for dates : {}".format(self.dates_to_scrape))


def main():
    scraper = SF_Court_Scraper(date_range=get_user_input_dates())
    scraper.get_records()


if __name__ == "__main__":
    main()
