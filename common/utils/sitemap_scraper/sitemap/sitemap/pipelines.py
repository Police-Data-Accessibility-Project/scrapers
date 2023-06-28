# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
import csv


class SitemapPipeline:
    def process_item(self, item, spider):
        return item


class CSVPipeline(object):
    """
    {'url': police_url[0],
     'last_modified_date': police_url[1] }
    """
    keys = ['url', 'last_modified_date']

    def __init__(self):
        now = datetime.datetime.now()
        current_date = now.strftime("%Y%m%d_%H%M%S")
        file_name = "output"
        self.infile = open("{}_{}.csv".format(current_date, file_name), "w")
        self.dict_writer = csv.DictWriter(self.infile, self.keys)
        self.dict_writer.writeheader()

    def process_item(self, item, spider):
        self.dict_writer.writerow(item)

    def close_spider(self, spider):
        self.infile.close()
