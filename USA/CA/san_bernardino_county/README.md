# San Bernardino County - Use of Force PDF Scraper

## To Use
1. Install python > 3.8
2. Install [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/). This package is the only external dependency (non python std-lib) used by this scraper.
3. Navigate to the scraper's base directory "~/.../PDAP-Scrapers/USA/CA/san_bernardino_county/"
4. Call the scraper with "python san_bernardino_uof_scraper.py"
5. Let the scraper run. It will take approx 20 seconds to collect the initial list of all links to scrape, after that you should see notification of each file collected in your console window/stdout.
6. Once the scraper is complete, review the files stored under the newly created "./data" directory located inside the san_bernardino_county folder.

## Notes
[San Bernardino County District Attorney - Use of Force Reviews page](https://sbcountyda.org/categories/news-releases/use-of-force-reviews/)

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```