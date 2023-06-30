import csv

with open('PDAP Data Sources.csv', encoding='utf-8-sig') as data:
    reader = csv.DictReader(data)
    reader = filter(lambda row: row['scraper_url'], reader)

    in_repo = filter(lambda row: 'Police-Data-Accessibility-Project' in row['scraper_url'], reader)
    not_in_repo = filter(lambda row: 'Police-Data-Accessibility-Project' not in row['scraper_url'], reader)

    for row in not_in_repo:
        print(row['scraper_url'])
