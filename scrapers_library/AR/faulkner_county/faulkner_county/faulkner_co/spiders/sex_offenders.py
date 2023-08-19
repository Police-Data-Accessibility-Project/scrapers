import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class SexOffendersSpider(scrapy.Spider):
    name = 'sex_offenders'
    allowed_domains = ['fcso.ar.gov']

    def start_requests(self):
        return self.collectURLs()

    def collectURLs(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)
        driver.get("https://www.fcso.ar.gov/sex_offenders.php")
        names  = driver.find_elements(By.XPATH, "//div[@id='name-panel']/a")
        
        list = []
        for name in names:
            try:
                name.click()
                view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'sex_offender_view')]")))
                request = scrapy.Request(url=view.get_attribute('href'), callback=self.parse)
                list.append(request)
            except:
                self.logger.error("Failed: " + name)

        driver.quit()

        return list

    def parse(self, response):
        item = {}

        item['name'] = self.extract_name(response)

        self.get_fields(response, item)

        item['offender_level'] = self.extract_offender_level(response)
        item['offense'] = self.extract_offense(response)

        yield item

    def extract_offender_level(self, response):
        offender_level_xpath = "normalize-space((//div[contains(@class, 'level_')])[1]/strong/text())"
        return response.xpath(offender_level_xpath).get().replace("\u00a0", "").replace("\u00A0", "").strip()

    def extract_offense(self, response):
        offense_xpath = "normalize-space((//div[contains(@class, 'level_')])[2]/p/text())"
        return response.xpath(offense_xpath).get().replace("\u00a0", "").replace("\u00A0", "").strip()

    def get_fields(self, response, item):
        x = response.xpath("(//div[@style='display:table-row'])")

        for row in x:
            value_xpath = "normalize-space(./div[@class='right-cell']/text())"
            value = row.xpath(value_xpath).get().replace("\u00a0", "").replace("\u00A0", "").strip()

            label_xpath = "normalize-space(./div[@class='left-cell']/strong/text())"
            label = row.xpath(label_xpath).get().replace(" / ", "_").replace(" ", "_").replace("/", "_").replace(":", "").lower()

            item[label] = value
            
        self.logger.debug(item)
        return item

    def extract_name(self, response):
        name_xpath = "normalize-space(//h2[@class='ptitles']/text())"
        return response.xpath(name_xpath).get().replace("\u00A0", "").strip()