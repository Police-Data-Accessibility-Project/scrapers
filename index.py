import csv


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
    md.write('<details>\n')
    md.write('\t<summary>In this repo</summary>\n')

    current_state = not_in_repo[0]['state']
    for row in not_in_repo:
        if current_state != row['state']:
            md.write('\t</details>\n')
            write_state_header(md, row)
            current_state = row['state']

    md.write('</details>\n')


    md.close()


def write_state_header(md, row):
    md.write('\t<details>\n')
    md.write(f'\t\t<summary>{row["state"]}</summary>\n')


def main():
    data = get_data()

    for row in data:
        in_repo_filter(row)

    write_md()

    #for row in not_in_repo:
        #print(row['state'])


if __name__ == '__main__':
    in_repo = []
    not_in_repo = []
    md = None

    main()