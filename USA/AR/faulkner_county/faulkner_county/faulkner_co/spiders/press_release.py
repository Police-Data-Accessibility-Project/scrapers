import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PressReleaseSpider(CrawlSpider):
    name = 'press_release'
    allowed_domains = ['fcso.ar.gov']
    start_urls = ['https://www.fcso.ar.gov/press']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='press-items']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='page_num' and text()='>'])[2]"), follow=True),
    )

    def parse_item(self, response):
        item = {}

        title_xpath = "//h2[@class='ptitles']/text()"
        item['title'] = response.xpath(title_xpath).get()

        image_link_xpath = "(//div[@id='cms-body-content']/p)[2]/img/@src"
        item['image_link'] = response.urljoin(response.xpath(image_link_xpath).get())

        text_xpath = "(//div[@id='cms-body-content']/p)[1]/text()"
        item['text'] = response.xpath(text_xpath).get()

        return item