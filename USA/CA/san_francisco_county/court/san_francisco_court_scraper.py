from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd
import time


class SF_Court_Scraper:
    """
    Scraper class for SF Court data
    """

    dates_to_scrape = []

    def __init__(self, date=None, date_range=None):
        """
        date or date_range can be entered.
        ---
        date: datetime.date("YYYY-MM-DD")
        date_range: tuple of two datetime.date values (start, end)
        ---
        Example date_range: (datetime.date("2021-02-01"), datetime.date("2021-03-01"))
        """
        self.sf_court_entry_link = r"https://webapps.sftc.org/captcha/captcha.dll?referrer=https://webapps.sftc.org/ci/CaseInfo.dll?"
        # Selenium timeout param in seconds. If this is too low we won't be able to complete the CAPTCHA before it times out.
        # A "wait" function could potentially be used instead of timeout; the timeout is nice because it will kill our driver if the CAPTCHA isn't completed.
        self.CAPTCHA_timeout = 30

        # If date_range is passed as a param, then we need to generate a list of date values between the start and end date passed
        if date_range:
            # Calculate all of the dates that we want to scrape from the SF Court portal, excluding weekends
            num_days_scraping_period = (date_range[1] - date_range[0]).days + 1
            self.dates_to_scrape = pd.date_range(
                date_range[0], periods=num_days_scraping_period
            )

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
            print("Timed out waiting for page to load")
            driver.close()
            return

        # We made it through the CAPTCHA!
        new_filings_menu_xpath = driver.find_element_by_id("ui-id-3").click()
        time.sleep(10)
        # End condition with driver, close browser
        if driver.window_handles:
            driver.close()

        return


def main():
    temp = SF_Court_Scraper(
        date_range=(
            datetime.strptime("2021-01-01", "%Y-%m-%d"),
            datetime.strptime("2021-01-05", "%Y-%m-%d"),
        )
    )
    print(temp.dates_to_scrape)


if __name__ == "__main__":
    main()
