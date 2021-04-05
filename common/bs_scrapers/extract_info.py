def extract_info(soup, configs):
    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(configs.web_path):
            continue
        print(link.get("href"))
        url = str(link["href"])
        name = url[url.rindex("/") :]

        with open("url_name.txt", "a+") as output:
            # This isn't really needed, but it's nice to have when debug is True
            if url not in output.read():
                if configs.domain_included == True:
                    output.write(url + ", " + name.strip("/") + "\n")
                elif configs.domain_included == False:
                    output.write(configs.domain + url + ", " + name.strip("/") + "\n")
    print("Done")
