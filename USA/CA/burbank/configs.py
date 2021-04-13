# Set to the page you want to scrape
webpage = "https://www.burbankpd.org/crime-information/daily-arrest-logs/?F_All=y"
"""
Click the links that lead to the files, and copy their paths.
**NOTE:** Ensure that files all match paths, otherwise remove a level until they match
Also ensure that domain stays the same
Verify on page that the href to the file contains the domain, if it doesn't, uncomment domain
"""
web_path = "/file.aspx?DocumentId"
# If the domain is not in the href, set to False, otherwise set it to True
domain_included = False
domain = "https://www.burbankpd.org"
# Set to desired sleep time
sleep_time = 5
# Are there any links on the page that you do not want? **ONLY FOR V3***
# Put a word found in them (the links you don't want) in this list. It can be one ore more words
non_important = ["alarm"]
# For devs:
debug = False
name_in_url=False
