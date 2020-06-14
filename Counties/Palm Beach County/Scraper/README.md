# Florida: Palm Beach County

## Installation

### Local installation

- install node
- extract these files into a folder
- navigate to that folder via terminal
- type "npm install"

That should install all the node npm packages needed to run the script. You can modify the settings in r.js./ line 51

Setting start to 0 should start you on the current day. Setting end to 1 should collect 2 days (day 0 & 1). I believe setting pages sets a max page count. There can be multiple pages per day.

- type "npm start" 

that will run the scraper in a custom chrome browser.


### Dockerized installation

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)

2. `cd Scraper`

3. `docker-compose build scraper`

4. `docker-compose up`