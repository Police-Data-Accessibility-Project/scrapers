"""

Script: sitemap_spider.py

Author: Nick (Discord- 'nick-o-rama#9923', Github- '@nfmcclure', email- 'nfmcclure@gmail.com')

Date: 2022-11-08

Purpose: Given a list of host URLs/domains. Get all sitemap XML information (sitemaps may be nested).

"""

import scrapy
import xmltodict


def nested_dict_values(my_dict, key_substrings=('',)):
    """
    Heavily Adapted from:
    https://stackoverflow.com/a/31439438/3123703

    Purpose: to navigate a nested dictionary (converted from sitemap.xml),
    And find any value (URL) that contains words in the tuple `key_substrings`).

    Also, return the 'lastmod' (last modified) date if exists.

    """
    for k, v in my_dict.items():
        if isinstance(v, dict):
            yield from nested_dict_values(v, key_substrings=key_substrings)
        elif isinstance(v, list):
            for element in v:
                yield from nested_dict_values(element, key_substrings=key_substrings)
        else:
            if isinstance(v, str):
                if any([ks in v for ks in key_substrings]):
                    datemod = my_dict.get('lastmod', None)
                    yield v, datemod


class GetsitemapSpider(scrapy.Spider):
    name = 'sitemapspider'
    # Depth limit set to 1, so we don't navigate away from the host domain sitemap--> sometimes sitemaps will link to
    #    the Google XML standards.
    DEPTH_LIMIT = 1
    RETRY_TIMES = 0

    def start_requests(self):
        # Read urls. NOTE: change this if you have a different file to read.
        with open('sample_host_sites.txt', 'r') as f:
            urls = f.readlines()
        urls = [url.strip() for url in urls]

        sitemap_urls = [url.strip('/') + '/sitemap.xml' for url in urls]
        for sm_url in sitemap_urls:
            yield scrapy.Request(url=sm_url, callback=self.parse)

    def parse(self, response):
        try:
            xml_dict = xmltodict.parse(response.text, encoding='iso-8859-1')
        except:
            try:
                xml_dict = xmltodict.parse(response.text, encoding='utf-8')
            except:
                xml_dict = {}

        # Get police URLs
        # TODO: update this with more/better keywords?
        police_keywords = ('police', 'cop')
        # Generator that returns: (url, last_modified_date_string), (url, last_modified_date_string), ...
        police_urls = nested_dict_values(xml_dict, key_substrings=police_keywords)
        for police_url in police_urls:
            yield {
                'url': police_url[0],
                'last_modified_date': police_url[1]
            }

        # Get more sitemap urls if exists:
        sitemap_urls = nested_dict_values(xml_dict, key_substrings=('sitemap',))
        sitemap_urls = [sm[0] for sm in sitemap_urls]

        if sitemap_urls is not None:
            for sm_url in sitemap_urls:
                yield scrapy.Request(sm_url, callback=self.parse)
