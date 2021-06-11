def extract_info(
    soup, configs, extract_name=False, name_in_url=True, configs_file=False, debug=False
):
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
            # print("href not startswith")
            # print(link)
            continue
        if debug:
            print("link: " + link.get("href"))

        url = str(link["href"])
        print(url)
        if extract_name == False:
            # print(" [?] extract_name is False")
            name = url[url.rindex("/") :]
        else:
            name = link.string
            # print(" [?] extract_name is True")
            # print(name)

        if not name_in_url:
            response = urllib.request.urlopen(domain + url)
            file_name, params = cgi.parse_header(
                response.headers.get("Content-Disposition", "")
            )
            name = file_name

        with open("url_name.txt", "a+") as output:
            if url not in output.read():
                if domain_included == True:
                    output.write(url + ", " + name.strip("/") + "\n")
                elif domain_included == False:
                    output.write(domain + url + ", " + name.strip("/") + "\n")
    print("   [*] Done extracting!")
