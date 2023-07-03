import csv


def get_data():
    with open('PDAP Data Sources.csv', encoding='utf-8-sig') as data:
        reader = list(csv.DictReader(data))
        reader.sort(key=lambda row: row['state'])
    return reader


def in_repo_filter(row):
    is_in_list = lambda list: row['name'] in [row['name'] for row in list]

    if 'Police-Data-Accessibility-Project' in row['scraper_url'] and not is_in_list(in_repo):
        in_repo.append(row)
    elif row['scraper_url'] and not is_in_list(not_in_repo):
        not_in_repo.append(row)


def write_md():
    md = open('scraper_index.md', 'w')
    md.write('# Scraper Index\n\n')
    
    md.write('<details>\n')
    md.write('\t<summary><font size="+2">In this repo</font></summary>\n')
    write_section(md, in_repo)
    md.write('</details>\n')

    md.write('<details>\n')
    md.write('\t<summary><font size="+2">Not in this repo</font></summary>\n')
    write_section(md, not_in_repo)
    md.write('</details>\n')

    md.close()


def write_section(md, section_data):
    current_state = 'Start'

    for row in section_data:
        new_state = current_state != row['state']
        if new_state and current_state != 'Start':
            md.write('\t</details>\n')
        if new_state:
            write_state_header(md, row)
            current_state = row['state']

        write_scraper(md, row)

    md.write('\t</details>\n')
    

def write_state_header(md, row):
    md.write('\t<details>\n')
    md.write(f'\t\t<summary><font size="+1">{row["state"]}</font></summary>\n')


def write_scraper(md, row):
    md.write('\t\t<details>\n')
    md.write(f'\t\t\t<summary><u>{row["name"]}</u></summary>\n')
    md.write(f'\t\t\t{"&emsp;" * 2}<b>Agency described:</b> {row["agency_described"]}<br>\n')
    md.write(f'\t\t\t{"&emsp;" * 2}<b>Record type:</b> {row["record_type"]}<br>\n')
    md.write(f'\t\t\t{"&emsp;" * 2}<b>Scraper URL:</b> <a href="{row["scraper_url"]}">{row["scraper_url"]}</a><br>\n')
    md.write(f'\t\t\t{"&emsp;" * 2}<b>State:</b> {row["state"]}<br>\n')
    if row['county']:
        md.write(f'\t\t\t{"&emsp;" * 2}<b>County:</b> {row["county"]}<br>\n')
    if row['municipality']:
        md.write(f'\t\t\t{"&emsp;" * 2}<b>Municipality:</b> {row["municipality"]}<br>\n')
    md.write(f'\t\t</details>\n')


def main():
    data = get_data()

    for row in data:
        in_repo_filter(row)

    write_md()


if __name__ == '__main__':
    in_repo = []
    not_in_repo = []

    main()