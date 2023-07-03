import csv
import re
from collections import OrderedDict


def get_data():
    with open('PDAP Data Sources.csv', encoding='utf-8-sig') as data_sources:
        reader = list(csv.DictReader(data_sources))
        reader.sort(key=lambda data_source: data_source['state'])
    return reader


def in_repo_filter(data_source):
    is_in_list = lambda list: data_source['name'] in [data_source['name'] for data_source in list]

    if 'Police-Data-Accessibility-Project' in data_source['scraper_url'] and not is_in_list(in_repo):
        in_repo.append(data_source)
    elif data_source['scraper_url'] and not is_in_list(not_in_repo):
        not_in_repo.append(data_source)


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
    national_data = []
    current_state = 'Start'

    for data_source in section_data:
        if not data_source['state'] or ',' in data_source['state']:
            national_data.append(data_source)
            continue

        new_state = current_state != data_source['state']
        if new_state and current_state != 'Start':
            md.write('\t</details>\n')
        if new_state:
            write_state_header(md, data_source['state'])
            current_state = data_source['state']

        write_scraper(md, data_source)

    md.write('\t</details>\n')
    
    write_state_header(md, 'National and multistate')

    remove_duplicates = lambda s: ", ".join(OrderedDict.fromkeys(s.split(',')))

    for data_source in national_data:
        if ',' in data_source['state']:
            data_source['agency_described'] = remove_duplicates(data_source['agency_described'])
            data_source['state'] = remove_duplicates(data_source['state'])
            data_source['county'] = remove_duplicates(data_source['county'])
            data_source['municipality'] = remove_duplicates(data_source['municipality'])
        elif not data_source['state']:
            data_source['state'] = 'USA'

        write_scraper(md, data_source)
    
    md.write('\t</details>\n')


def write_state_header(md, state):
    md.write('\t<details>\n')
    md.write(f'\t\t<summary><font size="+1">{state}</font></summary>\n')


def write_scraper(md, data_source):
    remove_state_code = lambda s: re.sub(r' - [A-Z]{2}$', '', s)

    md.write('\t\t<details>\n')
    name = remove_state_code(data_source['name'])
    md.write(f'\t\t\t<summary><u>{name}</u></summary>\n')

    agency = data_source['agency_described']
    if ',' not in agency:
        agency = remove_state_code(data_source['agency_described'])
        
    md.write(f'\t\t\t{"&emsp;" * 2}<b>Agency described:</b> {agency}<br>\n')
    md.write(f'\t\t\t{"&emsp;" * 2}<b>Record type:</b> {data_source["record_type"]}<br>\n')
    md.write(f'\t\t\t{"&emsp;" * 2}<b>Scraper URL:</b> <a href="{data_source["scraper_url"]}">{data_source["scraper_url"]}</a><br>\n')
    md.write(f'\t\t\t{"&emsp;" * 2}<b>State:</b> {data_source["state"]}<br>\n')
    if data_source['county']:
        md.write(f'\t\t\t{"&emsp;" * 2}<b>County:</b> {data_source["county"]}<br>\n')
    if data_source['municipality']:
        md.write(f'\t\t\t{"&emsp;" * 2}<b>Municipality:</b> {data_source["municipality"]}<br>\n')

    md.write(f'\t\t</details>\n')


def main():
    data_sources = get_data()

    for data_source in data_sources:
        in_repo_filter(data_source)

    write_md()


if __name__ == '__main__':
    in_repo = []
    not_in_repo = []

    main()