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
    md.write('\t<summary>In this repo</summary>\n\n')
    
    current_state = 'Start'
    for row in not_in_repo:
        new_state = current_state != row['state']
        if new_state and current_state != 'Start':
            md.write('\t\t- - -\n')
            md.write('\t</details>\n')
        if new_state:
            write_state_header(md, row)
            current_state = row['state']

        write_scraper(md, row)

    md.write('</details>\n')


    md.close()


def write_state_header(md, row):
    md.write('\t<details>\n')
    md.write(f'\t\t<summary>{row["state"]}</summary>\n\n')


def write_scraper(md, row):
    md.write('\t\t<details>\n')
    md.write(f'\t\t\t<summary>{row["name"]}</summary>\n\n')
    md.write(f'\t\t</details>\n')


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