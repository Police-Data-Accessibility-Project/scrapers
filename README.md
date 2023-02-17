<img src="https://user-images.githubusercontent.com/30379833/204395427-c8327551-a3c9-4363-8689-63880d72a495.png" width="200px">

# Welcome!

This is the GitHub home for the [Police Data Accessibility Project](https://pdap.io). We're assembling a toolkit and space for shared resources. People all over the country use these resources to collect public records about the U.S. criminal legal system.

This repository is also a guide to the countless ways we use scraper code to access data. ([What do we mean by web scraper?](https://docs.pdap.io/activities/terms-and-definitions))


[//]: # (Tempting to flesh this out in advance as something to work toward, and then adjust as necessary)
<details>
  <summary>Table of contents</summary>
</details>

# How to run a scraper
Right now, this requires some Python knowledge and patience. We're in the early stages: there's no automated scraper farm or fancy GUI yet.

[//]: # (We should have or point to a guide for No. 1; it can be tricky and annoying and it's in our power to make it less so)

[//]: # (And we should be much more specific about No. 4. Ideally, how someone installs something shouldn't impact how it works. But if we do want to keep that, we should have different paths for instructions so we can show folks step by step exactly what they need and what to expect)

1. Install Python. 
2. [Clone this repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
3. Find the scraper you wish to run. These are sorted geographically, so start by looking in `/USA/...`.
4. Run the `scraper.py` file with something like `python3 <scraper path>` depending on how you installed it.

## Did it work?

[//]: # (What do we mean here by "findings"? Just that it worked? If we're assuming analysis or exploration -- or impact! -- we could be clearer about that)

If it worked, discuss your findings in our [Discord](https://discord.gg/wMqex8nKZJ). If it didn't, make an issue in this repo or reach out in Discord.

# How to contribute
To write a scraper, start with [CONTRIBUTING.md](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/blob/main/CONTRIBUTING.md). Be sure to check out the [/common folder](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/tree/main/common/)!

For everything else, start with [docs.pdap.io](https://docs.pdap.io/).

## Resources

[//]: # (We should be clearer about these: Why do we like them? What problems would they help a contributor solve?)

Potentially useful tools. If you find something useful, or if one of these is out of date, make a PR!
- https://www.scrapingbee.com/
- https://github.com/CJWorkbench/cjworkbench
