
# run the scrapers for this agency

print('Running Chico - Daily Bulletins Scraper')
import chico_daily
print('Running Chico - Crimegraphics Bulletins Scraper')
import crimegraphics_bulletin

# then run the etl process
print('Running Chico - ETL')
import etl