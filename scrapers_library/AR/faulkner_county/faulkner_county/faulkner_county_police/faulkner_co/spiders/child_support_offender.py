import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from faulkner_co.items import ChildSupportOffenderItem


class ChildSupportOffenderSpider(CrawlSpider):
    name = 'child_support_offender'
    allowed_domains = ['fcso.ar.gov']
    start_urls = ['https://www.fcso.ar.gov/child-support-offenders']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="(//a[text()='>'])[1]"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        rows_xpath = "//div[@class='columns medium-6 text2']"
        rows = response.xpath(rows_xpath)

        for row in rows:
            item = ChildSupportOffenderItem()
            item['name'] = self.extract_name(row)
            item['age'] = self.extract_age(row)
            item['date'] = self.extract_date(row)
            item['bond'] = self.extract_bond(row)
            item['charges'] = self.extract_charges(row)

            yield item

    def extract_name(self, response):
        name_xpath = "./div/span[@class='ptitles warrant_data']/text()"
        return response.xpath(name_xpath).get()

    def extract_age(self, response):
        age_xpath = "./div/span[text()='Age: ']/following-sibling::text()"
        return response.xpath(age_xpath).get()

    def extract_date(self, response):
        date_xpath = "./div/span[text()='Date: ']/following-sibling::text()"
        return response.xpath(date_xpath).get()

    def extract_bond(self, response):
        bond_xpath = "./div/span[text()='Bond: ']/following-sibling::text()"
        return response.xpath(bond_xpath).get()

    def extract_charges(self, response):
        charges_xpath = "./div[@class='charge_desc']/text()"
        return response.xpath(charges_xpath).get()