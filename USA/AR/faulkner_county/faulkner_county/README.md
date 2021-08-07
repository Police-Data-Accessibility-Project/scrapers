# faulkner_co
A web scraper for the [Faulkner County, Arkansas police department](https://www.fcso.ar.gov/).

## Spiders
---
### child_support_offender
Scrapes items from Faulkner County's [list](https://www.fcso.ar.gov/child-support-offenders) of child-support offenders. Each entry on the website also includes a picture of the offender a link to which is not included in these results. It could be included in future iterations, but will require Selenium to retrieve.\
Class: [ChildSupportOffenderSpider](faulkner_co/spiders/child_support_offender.py)

### current_inmates
Scrapes items from Faulker County's current-inmate [roster](https://www.fcso.ar.gov/roster.php).\
Class: [CurrentInmatesSpider](faulkner_co/spiders/current_inmates.py)

### press_release
Scrapes text and image links from Faulker County's press-releases listed [here](https://www.fcso.ar.gov/press).\
Class: [PressReleaseSpider](faulkner_co/spiders/press_release.py)

### sex_offenders
Scrapes items from Faulkner County's [list](https://www.fcso.ar.gov/sex_offenders.php) of registered sex-offenders.\
Class: [SexOffendersSpider](faulkner_co/spiders/sex_offenders.py).

### warrants2
Scrapes [current and past](https://www.fcso.ar.gov/warrants.php) warrant information.\
Class: [Warrants2Spider](faulkner_co/spiders/warrants2.py)

## Items
---
Some of the items used in this project do not have corresponding python classes that represent them. In the case of the sex_offender spider
some of the offender-info pages had different fields from each other. It was easiest to implement a solution that added a field from the
page regardless of what it is and name it after the field to its left. It's left in the project because it may be implemented in the future.\
\
The definition of each item can be found in [items.py](faulkner_co/items.py)

### WarrantItem
```python
class WarrantItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    date = scrapy.Field()
    charges = scrapy.Field()
```
### ChildSupportOffenderItem
```python
class ChildSupportOffenderItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    date = scrapy.Field()
    bond = scrapy.Field()
    charges = scrapy.Field()
```
### InmateItem
Most fields are self-explanatory except maybe vinelink. [VINE](https://vinelink.com/#state-selection) is a victim notification system. 
Each inmate has an individual link that will take you to their profile on VINE where one can sign up for notifications concerning that inmate.
```python
class InmateItem(scrapy.Item):
    name = scrapy.Field()
    booking_number = scrapy.Field()
    age = scrapy.Field()
    gender = scrapy.Field()
    race = scrapy.Field()
    arresting_agency = scrapy.Field()
    booking_date = scrapy.Field()
    release_date = scrapy.Field()
    charges = scrapy.Field()
    vinelink = scrapy.Field()
```
### SexOffenderItem
```python
class SexOffenderItem(scrapy.Item):
    name = scrapy.Field()
    aka = scrapy.Field()
    address = scrapy.Field()
    dob = scrapy.Field()
    gender = scrapy.Field()
    hair = scrapy.Field()
    eyes = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    race = scrapy.Field()
    scars_marks_etc = scrapy.Field()
    additional_info = scrapy.Field()
    offender_level = scrapy.Field()
    offense = scrapy.Field()
```

## Pipelines
---
### FaulknerCoPipeline
There is a single item pipeline called [FaulknerCoPipeline](faulkner_co/pipelines.py). 
It initializes an array when a given spider is opened. Each item is appended to that array as they are passed down by the spider. 
When the spider closes, the array is dumped to a JSON file which is named based on the _type_ of spider passing it through the pipeline (also at this step the import [etl.py](faulkner_co/etl.py)) 
*   ChildSupportOffenderSpider  ==> sex_offenders.json
*   CurrentInmatesSpider        ==> inmates.json
*   SexOffendersSpider          ==> sex_offenders.json
*   Warrants2Spider             ==> warrants.json
*   PressReleaseSpider          ==> press_releases.json

JSON was chosen based purely on the author's personal preference and this pipeline can easily be updated to dump the items to a CSV file 
or a database instance (I reccomend MongoDB ;D)

## Setup and Run
---
### Selenium/chromedriver
The SexOffendersSpider uses selenium to retrieve a list of links through interactions with a Javascript interface on the page. Consequently, the chromedriver executable is required. It must be somewhere in the PATH of the profile executing the spider (or the system PATH). It may be downloaded [here](https://chromedriver.chromium.org/downloads).
### Executing spider crawl
From any directory within the scrapy project you may run:
```bash
$   scrapy crawl <spider name here>
```
Each spider's output is placed in the root directory of the project (I don't know how to change where it's written at the moment).

## Data Files
---
### [warrants.json](faulkner_co/warrants.json)
Data scraped by the [warrants2](#warrants2) spider.\
Format:
```json
{
    "name": "string",
    "age": "string",
    "date": "string",
    "charges": "string"
}
```

### [child_support_offenders.json](faulkner_co/child_support_offenders.json)
Data scraped by the [child_support_offender](#child_support_offender) spider.\
Format:
```json
{
    "name": "string",
    "age": "string",
    "date": "string",
    "bond": "string",
    "charges": "string"
}
```

### [inmates.json](faulkner_co/inmates.json)
Data scraped by the [current_inmates](#current_inmates) spider.\
Format:
```json
{
    "name": "string",
    "age": "string",
    "gender": "string",
    "race": "string",
    "charges": "string",
    "booking_number": "string",
    "arresting_agency": "string",
    "booking_date": "string",
    "release_date": "string"
}
```

### [sex_offenders.json](faulkner_co/sex_offenders.json)
Data scraped by the [sex_offenders](#sex_offenders) spider.\
Format:
```json
{
    "name": "string",
    "address": "string",
    "dob": "string",
    "gender": "string",
    "hair": "string",
    "eyes": "string",
    "height": "string",
    "weight": "string",
    "race": "string",
    "scars_marks_tattoos": "string",
    "additional_info": "string",
    "offender_level": "string",
    "offense": "string"
}
```

### [press_releases.json](faulkner_co/press_releases.json)
Data scraped by the [press_release](#press_release) spider.\
Format:
```json
{
    "title": "string",
    "image_link": "string",
    "text": "string"
}
```

### items.json
Any items that may find their way through the pipeline that doesn't belong to one of the above mentioned spiders is put
into a generic items.json file. This should never happen (except maybe during development).