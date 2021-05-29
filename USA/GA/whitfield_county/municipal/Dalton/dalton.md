This script has two functions, the first, `extract_info`, extracts the links containing documents, and saves the url and the document name to a file called `links.txt`
The second function, `get_files`, reads the link and name from `links.txt` and downloads the files.  

# More in depth explanations
 `extract_info` uses `urllib` to open the webpage, and then `BeautifulSoup4` to parse it. It then uses regex to finf all links that end with pdf or doc. It needs a few lines to be replaced with regex.

Added to datasets. Agency ID: ba737a45127044c2a6428d6c43fe0451
