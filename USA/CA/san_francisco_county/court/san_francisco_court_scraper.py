from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import re
import pandas as pd
import time


class SF_Court_Scraper:
    """
    Scraper class for SF Court data
    """

    dates_to_scrape = []
    session_id = ""

    def __init__(self, date=None, date_range=None):
        """
        date or date_range can be entered.

        date: datetime.date("YYYY-MM-DD")
        date_range: tuple of two datetime.date values (start, end)

        Example date_range: ("2021-01-01", "2021-02-01")
        """
        self.sf_court_entry_link = r"https://webapps.sftc.org/captcha/captcha.dll?referrer=https://webapps.sftc.org/ci/CaseInfo.dll?"
        # Selenium timeout param in seconds. If this is too low we won't be able to complete the CAPTCHA before it times out.
        # A "wait" function could potentially be used instead of timeout; the timeout is nice because it will kill our driver if the CAPTCHA isn't completed.
        self.CAPTCHA_timeout = 30

        # If date_range is passed as a param, then we need to generate a list of date values between the start and end date passed
        # We also want to have a check in place to see whether a single date was also passed. If this is the case, we'll use the single date value instead of the range and provide log output.
        if date_range and not date:
            # Calculate all of the dates that we want to scrape from the SF Court portal, excluding weekends
            # This is a bit funky. We're getting the difference between the start and end date, adding one to get all of the dates in the range (inclusive)
            num_days_scraping_period = (
                datetime.strptime(date_range[1], "%Y-%m-%d")
                - datetime.strptime(date_range[0], "%Y-%m-%d")
            ).days + 1
            # Use pandas to generate a list of dates based off of our specified range
            temp = pd.date_range(date_range[0], periods=num_days_scraping_period)
            # Format the dates : YYYY-MM-DD expected by SF court portal
            self.dates_to_scrape = temp.format(
                formatter=lambda x: x.strftime("%Y-%m-%d")
            )

        elif date:
            self.dates_to_scrape.append(date)

    # TODO : This is not a great implementation. We will rewrite "scrape" so that it just grabs the session id, stores it at class level and then closes.
    # TODO : Rename this method to something like generate session ID, change docstring to reference CAPTCHA
    def scrape(self):
        """
        Main scraper function for the San Francisco Court website
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

        print("CAPTCHA Completed! Session ID generated for scraping.")

        # TODO : This is a bad solution that relies on selenium browser. We can scrape the values after a session id has been generated with requests module
        # --- Clean this up
        try:
            element_present = EC.presence_of_element_located((By.ID, "ui-id-3"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print(
                "CAPTCHA completed but driver timed out waiting for main app page to load"
            )
            driver.close()
            return

        time.sleep(5)
        # We made it through the CAPTCHA! Move to the "Search by New Filings" menu
        driver.find_element_by_id("ui-id-3").click()
        time.sleep(3)
        # --- End Clean lol

        # End condition with driver, close browser
        if driver.window_handles:
            driver.close()

        return

    # TODO : Dummy method, need to be implemented
    def get_records(self, date):
        """
        This is the method that uses GET requests to call the SF court website once we've obtained a session token/id (stored at class level)

        date : For each specific set of records/GET request, we need a date provided (sample : date="2022-01-01")
        """
        # Sample URL : "https://webapps.sftc.org/ci/CaseInfo.dll/datasnap/rest/TServerMethods1/GetCasesWithFilings/2023-02-01/614B0E1B97DE9C565BE9D3D6DB091C77778EEB96/"

        return

    # TODO : Dummy method
    def parse_response(self):
        """
        For each response that we receive from our GET request, we need to parse them with REGEX to extract the required fields
        """
        return


def main():
    temp = SF_Court_Scraper(date="2022-01-01")
    temp.scrape()
    # temp = SF_Court_Scraper(date_range=("2022-01-01", "2022-01-05"))
    # print(temp.dates_to_scrape)


if __name__ == "__main__":
    main()
