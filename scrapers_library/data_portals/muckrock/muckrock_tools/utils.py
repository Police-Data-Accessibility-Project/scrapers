import re


def format_filename_json_to_csv(json_filename: str) -> str:
    '''
    Converts JSON filename format to CSV filename format.

    Args:
        json_file (str): A JSON filename string.

    Returns:
        csv_filename (str): A CSV filename string.

    '''
    csv_filename = re.sub(r'_(?=[^.]*$)', '-', json_filename[:-5]) + '.csv'

    return csv_filename
