import csv

in_repo = []
not_in_repo = []


def get_data():
    with open('PDAP Data Sources.csv', encoding='utf-8-sig') as data:
        reader = list(csv.DictReader(data))
        reader.sort(key=lambda row: row['state'])
    return reader


def in_repo_filter(row):
    if 'Police-Data-Accessibility-Project' in row['scraper_url']:
        in_repo.append(row)
    elif row['scraper_url']:
        not_in_repo.append(row)


def main():
    data = get_data()

    for row in data:
        in_repo_filter(row)

    for row in not_in_repo:
        print(row['state'])


if __name__ == '__main__':
    main()