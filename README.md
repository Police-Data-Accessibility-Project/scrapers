# Police Data Accessibility Project Scrapers
This repo contains the record scrapers (and associated tooling) to further the goals of the Police Data Accessibility Project. Thank you for your interest in contributing!

# Getting Started
## Quick start
1. [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo.
2. [Find a dataset to scrape](https://www.dolthub.com/repositories/pdap/datasets/), or [submit your own by following these DoltHub instructions](https://docs.google.com/document/d/1cxvH_O6XwXNmjs5oJi5gR5Y3mLnYENq6XBYbNrfz3ko/edit).
3. Make a copy of the template folder in the appropriate jurisdiction folder. Read more about structure below.
4. Code your scraper.
5. Scrape sample data from the source and add a truncated version to the folder so we understand the kind of data your scraper generates.
6. Complete the readme to the best of your ability.
7. Add the dolt repo to a config
8. Submit a Pull Request for approval.

## Approving scrapers
We require that scrapers be reviewed to meet our [legal guidelines](https://pdap-docs.readthedocs.io/en/latest/volunteers/resources/legal_restrictions.html). Checking that scrapers comply with our legal requirements is top priority. **Approve working legal scrapers.**

1. Review the scraper for [legal risk](https://pdap-docs.readthedocs.io/en/latest/volunteers/resources/legal_restrictions.html).
2. Test the scraper yourself to see whether it works.
3. If it works, **approve it**.
4. Make a comment if you have style suggestions. Better, share your skills by making a commit to their branch!

## Structure
Stick to the format of `USA/$STATE/$COUNTY/$RECORD_TYPE`. If there are state-level records being scraped, use `USA/$STATE/_State/$RECORD_TYPE`. Use underscores rather than spaces or dashes.

## Legal
Only scrapers that comply with our [legal guidelines](https://docs.google.com/document/d/1gjnH0S18iBI20K1pfs4M3wuMqcLE_ZSgt71ITUY2Fbk/edit) will be merged into this repo.

## General Guidelines
Python is preferred. If you use another language, please document your work.

Your scraper must comply with our [legal guidelines](https://docs.google.com/document/d/1gjnH0S18iBI20K1pfs4M3wuMqcLE_ZSgt71ITUY2Fbk/edit).

Everyone working on this project is using their free time. Please expect some back-and-forth communication when speaking to the individuals reviewing your PR's and be patient and respectful with us. The more work you do to test and validate that your scraper has met the contribution guidelines, the quicker we can accept it.

## Getting Help
The [#scrapers_general](https://policeaccessibility.slack.com/archives/C013XH00WHZ) slack channel is the place to start.

### Fields to scrape
**Note:** the naming convention for these fields may not be consistent across data sources. If any fields are not retrievable please fill it with "NA". 
* _id
* _state
* _county
* CaseNum
* FirstName
* MiddleName
* LastName
* Suffix
* DOB
* Race
* Sex
* ArrestDate
* FilingDate
* OffenseDate
* DivisionName
* CaseStatus
* DefenseAttorney
* PublicDefender
* Judge
* ChargeCount
* ChargeStatute
* ChargeDescription
* ChargeDisposition
* ChargeDispositionDate
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber
