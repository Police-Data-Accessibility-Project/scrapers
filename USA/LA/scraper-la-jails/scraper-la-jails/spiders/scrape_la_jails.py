from scrapy.spiders import Spider
from scrapy.http import FormRequest
from scrapy.crawler import CrawlerProcess


class MySpider(Spider):
    name = "scraper-la-jails"
    custom_settings = {
        "FEEDS": {
            "../data/la_jail_data/%(name)s_%(time)s.csv": {
                "format": "csv",
            }
        }
    }

    def start_requests(self):
        with open("../data/urls/la_jail_urls.csv") as f:
            for line in f:
                if not line.strip():
                    continue
                yield FormRequest(
                    url=line,
                    method="GET",
                    callback=self.parse,
                    formdata={"__EVENTTARGET": "lbShowAll"},
                )

    def parse(self, response):
        for tr in response.css("table#gvRoster tr")[1:]:
            yield {
                "arresting_agency_url": response.url,
                "inmate_race": tr.css("td:nth-child(4)::text")[0].get(),
                "inmate_sex": tr.css("td:nth-child(5)::text")[0].get(),
                "inmate_date_of_arrest": tr.css("td:nth-child(6)::text")[0].get(),
            }


def run_scraper():
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()


# import etl.py
