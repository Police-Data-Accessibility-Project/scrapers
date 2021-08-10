import scrapy


class ConwaypdSpider(scrapy.Spider):
    name = 'conwaypd'
    allowed_domains = ['conwaypd.org']
    start_urls = ['http://conwaypd.org/index.php/calls-for-service']

    def parse(self, response):
        html_items = response.xpath('//table[@id="at_303"]/tbody/tr')
        for row in html_items:
            yield {
                'call_number': row.xpath('./td[@class="ari-tbl-col-0"]/text()').get(),
                'case_number': row.xpath('./td[@class="ari-tbl-col-1"]/text()').get(),
                'address': row.xpath('./td[@class="ari-tbl-col-2"]/text()').get(),
                'call_time': row.xpath('./td[@class="ari-tbl-col-3"]/text()').get(),
                'incident_type': row.xpath('./td[@class="ari-tbl-col-4"]/text()').get()
            }
