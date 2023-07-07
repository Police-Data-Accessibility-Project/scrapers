import csv
import re
from collections import OrderedDict


def get_data():
    """Retrieve data from the csv file.

    Returns:
        list: List of dictionaries of data sources sorted by state code.
    """
    with open('common/utils/scraper_index/PDAP Data Sources.csv', encoding='utf-8-sig') as data_sources:
        reader = list(csv.DictReader(data_sources))
        # Sort by state code
        reader.sort(key=lambda data_source: data_source['state'])
    return reader


def in_repo_filter(data_source):
    """Filters data sources between whether or not they're in the PDAP repository.

    Args:
        data_source (dict): Data source to be sorted.
    """

    """Checks for duplicate names"""
    is_in_list = lambda list: data_source['name'] in [data_source['name'] for data_source in list]

    if 'Police-Data-Accessibility-Project' in data_source['scraper_url'] and not is_in_list(in_repo):
        in_repo.append(data_source)
    elif data_source['scraper_url'] and not is_in_list(not_in_repo):
        not_in_repo.append(data_source)


def write_md():
    """Write to the markdown file"""
    md = open('INDEX.md', 'w')
    md.write('# Scraper Index\n\n')

    # In this repo section
    write_section(md, in_repo, header='In this repo')

    # Not in this repo section
    write_section(md, not_in_repo, header='Not in this repo')

    md.close()


def write_section(md, section_data, header):
    """Write data for a particular section.

    Args:
        md (TextIOWrapper): Markdown file to write to.
        section_data (list): List of dictionaries of data sources sorted.
        header (String): Header, either In this repo or Not in this repo
    """
    national_data = []
    current_state = 'Start'

    md.write('<details>\n')
    md.write(f'\t<summary><font size="+2">{header}</font></summary>\n')

    for data_source in section_data:
        # Sort out national and multistate data sources
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

    if national_data:
        # Write national and multistate data section
        md.write('\t</details>\n')
        
        write_state_header(md, 'National and multistate')

        """Removes duplicate entries from a string"""
        remove_duplicates = lambda s: ", ".join(OrderedDict.fromkeys(s.split(',')))

        for data_source in national_data:
            is_multistate = ',' in data_source['state']
            if is_multistate:
                data_source['agency_described'] = remove_duplicates(data_source['agency_described'])
                data_source['state'] = remove_duplicates(data_source['state'])
                data_source['county'] = remove_duplicates(data_source['county'])
                data_source['municipality'] = remove_duplicates(data_source['municipality'])
            elif not data_source['state']:
                data_source['state'] = 'USA'

            write_scraper(md, data_source)
        
    md.write('\t</details>\n')
    md.write('</details>\n')


def write_state_header(md, state):
    """Write a new state header.

    Args:
        md (TextIOWrapper): Markdown file to write to.
        state (str): State code.
    """
    md.write('\t<details>\n')
    md.write(f'\t\t<summary><font size="+1">{state}</font></summary>\n')


def write_scraper(md, data_source):
    """Write scraper information in the following format:
        Agency described:\n
        Record type:\n
        Scraper URL:\n
        State:\n
        County:\n
        Municipality:

    Args:
        md (TextIOWrapper): Markdown file to write to.
        data_source (dict): Data source.
    """

    """Removes redundant trailing state code"""
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