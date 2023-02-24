# San Francisco Court Portal Scraper
### V1 : Written by Douglas S. Krouth
## Usage Notes
1. Move to SF scraper directory (PDAP-Scrapers/USA/CA/san_francisco/court/).
2. Call the script with "python san_francisco_court_scraper.py".
3. Enter START_DATE and END_DATE values in python console that appears. Ensure the following
   1. START_DATE and END_DATE are in the format "YYYY-MM-DD" *quotes excluded (example... START_DATE : 2022-02-03)
   2. START_DATE is before END_DATE calendar value (example... START_DATE : 2022-02-04  --  END_DATE : 2022-01-02 ... would not work as the START_DATE is less than END_DATE)
4. Wait for a pop-up screen (usually a few seconds) that will present a "I'm Not a Robot" CAPTCHA form. Complete this carefully to save yourself time.
5. Let the scraper run for the selected range of dates provided.
6. Observe output data in ./data directory. This directory will contain the scraped dataset and the list of all dates scraped.
   1. NOTE : This scraper only uses business dates and excludes weekends. Holidays may slip in with a single record value marked "No Cases Found for /<DATE/>", this can be handled in post-processing or you can open an issue in GitHub if this is causing extensive issues.

## Caveats
1. **DO NOT use this scraper to retrieve multiple years worth of data/records at a time!** At the very least, split the scraping sessions either into multiple days/weeks to prevent overloading/overuse of the SF court portal. Another suggestion on this would be to run different batches (date ranges desired) of the scraper throughout the day, preferably early morning/evenings (GMT-8 : PST).
2. I have not run into any issues with the SF Court Portal blocking my IP Address; however, I have been cautious to not scrape hundreds of dates at a time. There is discernment and caution required on the user's behalf to ensure that they use this tool responsibly and in an ethical fashion that doesn't restrict functionality of the target website (SF Court Portal).
3. This tool does not handle best-practice implementation for the output of the scraped data. Be aware that multiple runs of different date ranges will result in a single dataset that has just been appended to. If there are specific requests to present the data in a different format (custom filenames, uuid file indicators, etc.) please submit a GitHub issue.
4. If issues/bugs are found, reach out via GitHub Issue or contact package maintainers.


# Source info
The San Francisco Court Cortal has a reCAPTCHA that prohibits reuse of session ID past a certain time frame. This implementation will open a Selenium page, allow the user to click the reCAPTCHA and then it will run the scraper to collect records.

Records start as early as "1996-01-01" (Jan 1st, 1996).

Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if something has changed.

## Data refresh rate
Daily refresh, appears to be incremental? Could also be a batch process, not entirely sure.

## Legal
No robots.txt found. Site uses CAPTCHA session validation. We make no attempt to obfuscate and/or damage this CAPTHCA system - it is the responsibility of the user to complete the CAPTCHA session for each scraping period or if the scraper needs to generate a new session ID for whatever reason.

## Fields being collected:
- Filing Date
- Case Number
- Case Name

## Fields unobtainable within our legal guidelines:
N/A

## Data uniformity
No issues found.

# Sample response
Sample response from SF Court portal stored under *sample_response_sf_court_portal.json*. Names of cases have been obfuscated, case numbers were kept intact.

# Court Portal Link
[SF Court Portal](https://webapps.sftc.org/captcha/captcha.dll?referrer=https://webapps.sftc.org/ci/CaseInfo.dll?)