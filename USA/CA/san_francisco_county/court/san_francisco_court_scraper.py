from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import time


class SF_Court_Scraper:
    """
    Scraper class for SF Court data
    """

    date_range = []

    def __init__(self, date=None, date_range=None):
        '''
        date or date_range can be entered.
        ---
        date: datetime.date("YYYY-MM-DD")
        date_range: tuple of two datetime.date values (start, end)
        ---
        Example date_range: ("2021-02-01", "2021-03-01")
        '''
        self.sf_court_entry_link = r"https://webapps.sftc.org/captcha/captcha.dll?referrer=https://webapps.sftc.org/ci/CaseInfo.dll?"
        # Selenium timeout param in seconds. If this is too low we won't be able to complete the CAPTCHA before it times out.
        # A "wait" function could potentially be used instead of timeout; the timeout is nice because it will kill our driver if the CAPTCHA isn't completed.
        self.CAPTCHA_timeout = 30

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

    def check_dates(self):
        if not self.check_dates:
            print("Dates empty. Scraping for today.")
        else:
            


def main():
    SF_Court_Scraper().scrape()


if __name__ == "__main__":
    main()
