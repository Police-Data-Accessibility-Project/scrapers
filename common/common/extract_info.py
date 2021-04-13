def extract_info(soup, configs, extract_name=False):
    for link in soup.findAll("a"):
        if link.get("href") is None:
            continue
        if not link["href"].startswith(configs.web_path):
            continue
        print(link.get("href"))
        url = str(link["href"])
        if extract_name == False:
            name = url[url.rindex("/") :]
        else:
            name = link.string
            print(name)

        with open("url_name.txt", "a+") as output:
            if url not in output.read():
                if configs.domain_included == True:
                    output.write(url + ", " + name.strip("/") + "\n")
                elif configs.domain_included == False:
                    output.write(configs.domain + url + ", " + name.strip("/") + "\n")
    print("Done")
