# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class ConwayPdPipeline:
    items = []

    def open_spider(self, spider):
        self.file = open('service_calls.json', 'w')

    def close_spider(self, spider):
        self.file.write(json.dumps(self.items))
        self.file.close()

    def process_item(self, item, spider):
        self.items.append((ItemAdapter(item).asdict()))
        return item
