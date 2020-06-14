# Florida: Palm Beach County

This Scraper was built in JS before Python was decided as a project language.

## Local Usage

### Installation

- Install node
- `cd scraper`
- `npm install`

That should install all the node npm packages needed to run the script. You can modify the settings in r.js./ line 51

Setting start to 0 should start you on the current day. Setting end to 1 should collect 2 days (day 0 & 1). I believe setting pages sets a max page count. There can be multiple pages per day.

### Running
- `cd scraper`
- `npm start` 

This will run the scraper in a custom Chrome browser.

## Dockerized Usage

### Building Image

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- `cd scraper`
- `docker-compose build` 

### Running Container
- `docker-compose up` 