This script has two functions, the first, `extract_info`, extracts the links containing documents, and saves the url and the document name to a file called `links.txt`
The second function, `get_files`, reads the link and name from `links.txt` and downloads the files.  

# More in depth explanations
 `extract_info` uses `urllib` to open the webpage, and then `BeautifulSoup4` to parse it. It then uses regex to finf all links that end with pdf or doc. It needs a few lines to be replaced with regex.

# Setup
 Set `webpage` to the page with the pdf lists


 Open a few pdfs and get the common file path for them, and set that as `web_path`


 Set the `domain` to the beginning of the document host.


 If the site has a set crawler time under it's `robots.txt`, set `sleep_time` to it's value. Otherwise, just leave it at `5`

If this does not make sense, try checking the comments within the code.
 Working example can be found [here](https://github.com/CaptainStabs/Scrapers/blob/master/USA/CA/alameda/alameda_scraper.py)
