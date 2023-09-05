# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ConwayPdItem(scrapy.Item):
    call_number = scrapy.Field()
    case_number = scrapy.Field()
    address = scrapy.Field()
    call_time = scrapy.Field()
    incident_type = scrapy.Field()
    pass
