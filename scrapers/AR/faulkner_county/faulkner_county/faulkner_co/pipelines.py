# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from faulkner_co.spiders.warrants2 import Warrants2Spider
from faulkner_co.spiders.child_support_offender import ChildSupportOffenderSpider
from faulkner_co.spiders.current_inmates import CurrentInmatesSpider
from faulkner_co.spiders.sex_offenders import SexOffendersSpider
from faulkner_co.spiders.press_release import PressReleaseSpider
import json


class FaulknerCoPipeline:
    items = []

    def open_spider(self, spider):
        # since this pipeline is run for all items, we check here to see what type of 
        # spider is being passed in and name the output file accordingly

        if isinstance(spider, Warrants2Spider):
            self.file = open('faulkner_co/warrants/warrants.json', 'w')
        elif isinstance(spider, ChildSupportOffenderSpider):
            self.file = open('faulkner_co/child_support_offenders/child_support_offenders.json', 'w')
        elif isinstance(spider, CurrentInmatesSpider):
            self.file = open('faulkner_co/inmates/inmates.json', 'w')
        elif isinstance(spider, SexOffendersSpider):
            self.file = open('faulkner_co/sex_offenders/sex_offenders.json', 'w')
        elif isinstance(spider, PressReleaseSpider):
            self.file = open('faulkner_co/press_releases/press_releases.json', 'w')
        else:
            self.file = open('items.json', 'w')

    def close_spider(self, spider):
        self.file.write(json.dumps(self.items))
        self.file.close()

    def process_item(self, item, spider):
        self.items.append(ItemAdapter(item).asdict())
        return item