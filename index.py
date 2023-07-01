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


def write_md():
    md = open('scraper_index.md', 'w')
    md.write('# Scraper Index\n\n')


def main():
    data = get_data()

    for row in data:
        in_repo_filter(row)

    write_md()

    #for row in not_in_repo:
        #print(row['state'])


if __name__ == '__main__':
    main()