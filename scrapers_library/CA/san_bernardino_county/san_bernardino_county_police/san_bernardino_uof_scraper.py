import requests
from bs4 import BeautifulSoup
import re
import time
import os
from pathlib import Path


def scrape():
    """
    The "driver" function. Grabs all pdf links,
    """
    # Create data directory in local if it isn't already present
    # TODO : Do we want a param to pass in a custom dir for users?
    if not os.path.exists("./data/"):
        os.mkdir("./data/")

    # Fetch the links for the individual use of force review pages
    uof_ind_case_review_links = _get_uof_review_links()

    # Go to each case review page and grab whatever pdf's are provided there
    files_collected_incr = 0
    for case_review_page_link in uof_ind_case_review_links:
        html = requests.get(case_review_page_link).content
        soup = BeautifulSoup(html, features="html.parser")
        # Some pages had duplicate pdf links in the html; to get around this, use a set to enforce distinct values
        pdf_links = set()
        for i in set(soup.find_all("a")):
            # Get all links
            temp_link = i.get("href")
            # For each distinct pdf, we put the link in the set of pdf's that we'll scrape in the next step
            if temp_link.endswith("pdf"):
                pdf_links.add(temp_link)

        # Download the pdfs
        # For each use of force incident page, there should be at least one pdf available. We want to fetch those download links and then retrieve the file
        # This loop is to iterate through each pdf found on a single uof page
        for file_link in pdf_links:
            # We try to request the uof document page 3 times
            tries = 3
            for try_value in range(tries):
                try:
                    output_file_name = Path(file_link).name
                    with open("./data/{}".format(output_file_name), "wb") as f:
                        response = requests.get(file_link)
                        # Write to pdf
                        f.write(response.content)
                    files_collected_incr += 1
                    print(
                        "Retrieved {}. ({} of {} files collected)".format(
                            output_file_name,
                            files_collected_incr,
                            (len(uof_ind_case_review_links) + 1),
                        )
                    )
                    # Courtesy sleep timer
                    time.sleep(2)
                except KeyError as e:
                    time.sleep(2)
                    if try_value < tries - 1:  # i is zero indexed
                        continue
                    else:
                        raise
                break


def _get_uof_catalog_pages():
    """
    Helper method to get use of force catalog pages from San Bernardino site. Fetches base page, calculates number of pages based on results param located at top of page under "<numeric> results"
    """
    # Get the number of pages from the "post-results field on the "Category: Use of Force Reviews" page
    try:
        uof_page = requests.get(
            "https://sbcountyda.org/categories/news-releases/use-of-force-reviews/"
        ).content
        soup = BeautifulSoup(uof_page, features="html.parser")
        # 10 links shown per page
        number_of_pages = (
            int(
                re.search(
                    "\d*", soup.find_all("div", {"class": "post-results"})[0].text
                ).group()
            )
            % 10
        )
        # Generate a list of base pages that we'll need to call for pdf reports
        base_pages = [
            "https://sbcountyda.org/categories/news-releases/use-of-force-reviews/page/{}/".format(
                i
            )
            for i in range(1, number_of_pages + 1)
        ]
        return base_pages
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def _get_uof_review_links():
    """
    For each instance of UOF documented by the court, there is an individual page stored on the SB website. This method gives those links, which will then have a link to a pdf of the court doc and police report.
    """
    # Get links to each individiual uof case filing page
    catalog_pages = _get_uof_catalog_pages()
    print("Fetched {} Use of Force Catalog pages".format(len(catalog_pages)))
    uof_links = []
    # For each catalog page, we want to grab the set of individual links on each.
    for cat in catalog_pages:
        # We try to request the catalog page 3 times
        tries = 3
        for try_value in range(tries):
            try:
                ind_uof_page = requests.get(cat).content
                soup = BeautifulSoup(ind_uof_page, features="html.parser")
                for i in soup.find_all(
                    "h2", {"class": "entry-title bolt-highlight-font"}
                ):
                    regex_match = re.search(r"\<a href=.* rel", str(i)).group()
                    # Strip head and tail of match to get just the link. There's probably a better way to search this with bs4
                    link_cleaned = (
                        str(regex_match).replace('<a href="', "").replace('" rel', "")
                    )
                    uof_links.append(link_cleaned)
                # Courtesy sleep timer
                time.sleep(2)
            except KeyError as e:
                time.sleep(1)
                if try_value < tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break

    if not os.path.exists("./data/"):
        os.mkdir("./data/")

    # Make a record of all the links scraped in a .txt file
    with open(r"./data/uof_links_scraped.txt", "w", newline="") as f:
        for i in uof_links:
            f.write("%s\n" % i)

    print(
        "Fetched {} links to individual Use of Force Case Review pages".format(
            len(uof_links)
        )
    )

    return uof_links


def main():
    print("--- SCRAPER STARTING ---")
    scrape()
    print("--- SCRAPER COMPLETE ---")


if __name__ == "__main__":
    main()
