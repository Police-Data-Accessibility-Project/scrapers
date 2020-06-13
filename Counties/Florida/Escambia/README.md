# Florida: Escambia County

Escambia County uses a Benchmark portal by Pioneer Technology .

* There is a very simple addition captcha.
* There are search filters for date ranges, which greatly simplifies finding cases.
* Case types can be filtered, meaning we can ignore irrelevant cases types.
* No search can give more than 5000 results, meaning searches will need to be specific enough to restrict cases below 5000.


## Installation

TODO (Scraper not written yet)

## Args

TODO (Scraper not written yet)

### Search Method: Case Number or Date Range
There are 2 viable ways to search for cases. Case Number or Date Range.

1. Date Range

    Unlike Bay County, Escambia County's version of Benchmark allows for searching a date range. This significantly reduces the number of searches, and therefore captchas that need to be solved.
    
    A date range like 01/01/2019 to 01/07/2019 could be used to scrape in 7-day windows. 
    
    It is important to adjust the date selection or court/case/party type settings to give fewer than 5000 results at a time.

2. Case Number

    `The Case Numbers used for searching this portal are not the same as the Uniform Case Numbering System. Store the Portal Case Number in 'PortalID' and the Uniform Case Number in 'CaseNum'.`

    The portal's case numbers looks like this: 2019 TR 000001. Let's decompose this...

    The first four digits **2019** signify the year of filing.

    The next two characters **TR** signify the case type.

    The following six digits **000001** signify the case number that year. This was the first traffic case filed that year.

    The next 2-4 characters signify the court filing type. This does not need to be included in the search.

    Cases can be opened iteratively by searching 2019 TR 000001, 2019 TR 000002, 2019 TR 000003, ... until no case is found.

    Unfortunately, there are some gaps in the data where a case is missing. I'm unsure for the reason for this, perhaps the case has not concluded, or it was removed.

    In this scenario, `missing-threshold` is defined, where after N missing cases, it is assumed all cases for that year have been explored.



### Solving Captcha

Automated captcha solving is disabled by default.

This County uses the same addition-based Captcha system as in Bay County.

For more details, check Bay County's README.md, or look at `common/captcha/benchmark/BenchmarkAdditionSolver.py`
