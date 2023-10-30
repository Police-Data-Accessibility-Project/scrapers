import logging
import sys


def extract_info(soup, configs, extract_name=False, name_in_url=True, configs_file=False, debug=False):
    """
    Extract information from supplied beautiful soup
    :param soup: BeautifulSoup object
    :param configs: dict of configuration
    :param extract_name: whether to extract name from url (default false)
    :param name_in_url: whether the file's name is in the url (default true)
    :param configs_file: reverse compatbility, leave alone (default false)
    :param debug: whether to print debug information (default false)
    """
    if debug:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    if not name_in_url:
        import cgi
        import urllib

    # Check added for backwards compatibility
    if not configs_file:  # Default setting
        web_path = configs["web_path"]
        domain = configs["domain"]
        domain_included = configs["domain_included"]
    else:
        web_path = configs.web_path
        domain = configs.domain
        domain_included = configs.domain_included

    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(web_path):
            # Not really sure why I added these in commit 986357286bc98bc154f2333ae75934be4e5df00d,
            # But they were causing tons of terminal puke.
            continue
            logging.debug("link: " + link.get("href"))

        url = str(link["href"])

        logging.info("URL: " + str(url))

        print(url)
        
        if not extract_name:
            name = url[url.rindex("/") :]
        else:
            name = link.string

        if not name_in_url:
            response = urllib.request.urlopen(domain + url)
            file_name, params = cgi.parse_header(response.headers.get("Content-Disposition", ""))
            name = file_name

        with open("url_name.txt", "a+") as output:
            if url not in output.read():
                if domain_included == True:
                    output.write(url + ", " + name.strip("/") + "\n")
                elif domain_included == False:
                    output.write(domain + url + ", " + name.strip("/") + "\n")
    print("   [*] Done extracting!")
