# Police Data Accessibility Project Scrapers
This repo contains the record scrapers (and associated tooling) to further the goals of the Police Data Accessibility Project. Thank you for your interest in contributing!

# Getting Started
## Quick start
1. [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo.
2. Make a copy of the template folder in the appropriate jurisdiction folder.
3. Code your scraper.
4. Scrape sample data from the source and add a truncated version to the folder so we understand the kind of data your scraper generates.
5. Complete the readme to the best of your ability.
6. If you know how to use Splunk, complete the config file.
7. Submit a Pull Request for approval.

## Legal
Only scrapers that comply with our [legal guidelines](https://docs.google.com/document/d/1gjnH0S18iBI20K1pfs4M3wuMqcLE_ZSgt71ITUY2Fbk/edit) will be merged into this repo.

## General Guidelines
Python is preferred. If you use another language, please document your work.

Your scraper must follow these [legal guidelines](https://docs.google.com/document/d/1gjnH0S18iBI20K1pfs4M3wuMqcLE_ZSgt71ITUY2Fbk/edit).

Everyone working on this project is using their free time. Please expect some back-and-forth communication when speaking to the individuals reviewing your PR's and be patient and respectful with us. The more work you do to test and validate that your scraper has met the contribution guidelines, the quicker we can accept it.

## Getting Help
The #scrapers-general slack channel is the place to start.

### Known datasets

This [dataset catalogue](https://docs.google.com/spreadsheets/d/1A0iTx7N-qVH2fms3Gmaf8RbnTpJPjgSoLPEa1o-J6J8/edit#gid=0&fvid=1660736644) is how we track potential sources.

### Fields to scrape

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
