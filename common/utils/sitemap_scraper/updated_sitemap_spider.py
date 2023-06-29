import xmltodict
import requests
import csv
from datetime import datetime as dt


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


def parse(response):
    try:
        xml_dict = xmltodict.parse(response.text, encoding='iso-8859-1')
    except:
        try:
            xml_dict = xmltodict.parse(response.text, encoding='utf-8')
        except:
            xml_dict = {}

    # Get URLs
    # TODO: update this with more/better keywords?
    tld_keywords = ('.us', '.gov')
    # Returns: (url, last_modified_date_string), (url, last_modified_date_string), ...
    tld_urls = nested_dict_values(xml_dict, key_substrings=tld_keywords)
    for tld_url in tld_urls:
        yield {
            'url': tld_url[0],
            'last_modified_date': tld_url[1]
        }

    # Get more sitemap urls if exists:
    sitemap_urls = nested_dict_values(xml_dict, key_substrings=('sitemap',))
    sitemap_urls = [sm[0] for sm in sitemap_urls]

    if sitemap_urls is not None:
        return sitemap_urls
    
    return []


def core():
    with open('sample_host_sites.txt', 'r') as f:
        urls = f.readlines()
    urls = [url.strip() for url in urls]

    sitemap_urls = [url.strip('/') + '/sitemap.xml' for url in urls]
    scraped_urls = []
    for sm_url in sitemap_urls:
        try:
            response = requests.get(sm_url)
            scraped_urls.extend(parse(response))
        except:
            continue            

    current_time = dt.now()
    current_time_str = current_time.strftime("%Y%m%d_%H%M%S")
    with open(f"{current_time_str}_output.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, ["url", "last_modified_date"], delimiter=",")
        writer.writeheader()
        writer.writerows(scraped_urls)

    return "Sitemaps scraped successfully!"


if __name__ == '__main__':
    print(core())