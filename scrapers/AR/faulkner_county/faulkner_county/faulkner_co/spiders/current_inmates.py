import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from faulkner_co.items import InmateItem


# Actually crawls both the 'Current Inmates' and '48-hour Hold Inmates' pages
class CurrentInmatesSpider(CrawlSpider):
    name = 'current_inmates'
    allowed_domains = ['fcso.ar.gov']
    start_urls = ['https://www.fcso.ar.gov/roster.php', 'http://https://www.fcso.ar.gov/roster.php?released=1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[contains(@aria-label, 'View Profile')]"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[text()='>'])[2]"), follow=True),
    )

    def parse_item(self, response):
        
        item = InmateItem()
        item['name'] = self.extract_name(response)
        item['age'] = self.extract_age(response)
        item['gender'] = self.extract_gender(response)
        item['race'] = self.extract_race(response)
        item['charges'] = self.extract_charges(response)
        item['booking_number'] = self.extract_booking_number(response)
        item['arresting_agency'] = self.extract_arresting_agency(response)
        item['booking_date'] = self.extract_booking_date(response)
        item['release_date'] = self.extract_release_date(response)

        yield item

    def extract_booking_number(self, response):
        booking_number_xpath = "(//div[@class='cell inmate_profile_data_content'])[1]/text()"
        return response.xpath(booking_number_xpath).get()

    def extract_name(self, response):
        name_xpath = "//span[@class='ptitles']/text()"
        return response.xpath(name_xpath).get()

    def extract_age(self, response):
        age_xpath = "(//div[@class='cell inmate_profile_data_content'])[2]/text()"
        return response.xpath(age_xpath).get()

    # 'Gender' is their word, not mine. 
    # This is Arkansas so they probably meant sex. I doubt they know the difference.
    def extract_gender(self, response):
        gender_xpath = "(//div[@class='cell inmate_profile_data_content'])[3]/text()"
        return response.xpath(gender_xpath).get()

    def extract_race(self, response):
        gender_xpath = "(//div[@class='cell inmate_profile_data_content'])[4]/text()"
        return response.xpath(gender_xpath).get()

    def extract_arresting_agency(self, response):
        arresting_agency_xpath = "(//div[@class='cell inmate_profile_data_content'])[5]/text()"
        return response.xpath(arresting_agency_xpath).get()

    def extract_booking_date(self, response):
        booking_date_xpath = "(//div[@class='cell inmate_profile_data_content'])[6]/text()"
        return response.xpath(booking_date_xpath).get()

    def extract_release_date(self, response):
        release_date_xpath = "(//div[@class='cell inmate_profile_data_content'])[7]/span/text()"
        return response.xpath(release_date_xpath).get()

    def extract_charges(self, response):
        charges_xpath = "(//div[@class='cell inmate_profile_data_content'])[8]/span/text()"
        return response.xpath(charges_xpath).get()