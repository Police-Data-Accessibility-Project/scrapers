def extract_info(soup, configs, extract_name=False, name_in_url=True):
    if not name_in_url:
        import cgi
        import urllib

    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(configs.web_path):
            print("href not startswith")
            print(link)
            continue
        print("link: " + link.get("href"))
        url = str(link["href"])
        if extract_name == False:
            # print(" [?] extract_name is False")
            name = url[url.rindex("/") :]
        else:
            name = link.string
            # print(" [?] extract_name is True")
            # print(name)
        if not name_in_url:
            response = urllib.request.urlopen(configs.domain + url)
            file_name, params = cgi.parse_header(
                response.headers.get("Content-Disposition", "")
            )
            name = file_name

        with open("url_name.txt", "a+") as output:
            if url not in output.read():
                if configs.domain_included == True:
                    output.write(url + ", " + name.strip("/") + "\n")
                elif configs.domain_included == False:
                    output.write(configs.domain + url + ", " + name.strip("/") + "\n")
    print("   [*] Done extracting!")
