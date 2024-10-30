import sqlite3
import pandas as pd
import json
import argparse
import os
from typing import Union, List, Dict

check_results_table_query = '''
                SELECT name FROM sqlite_master
                WHERE (type = 'table')
                AND (name = 'results')
                '''

search_foia_query = '''
        SELECT * FROM results
        WHERE (title LIKE ? OR tags LIKE ?)
        AND (status = 'done')
        '''


def parser_init() -> argparse.ArgumentParser:
    '''
    Initializes the argument parser for search_foia_data_db.py.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    '''

    parser = argparse.ArgumentParser(
        description='Search foia_data.db and generate a JSON file of resulting matches')
    parser.add_argument('--search_for', type=str, required=True, metavar='<search_string>',
                        help='Provide a string to search foia_data.db')

    return parser


def search_foia_db(search_string: str) -> Union[pd.DataFrame, None]:
    '''
    Searches the foia_data.db database for FOIA request entries matching the provided search string.

    Args:
        search_string (str): The string to search for in the `title` and `tags` of the `results` table.

    Returns:
        Union[pandas.DataFrame, None]:
            - pandas.DataFrame: A DataFrame containing the matching entries from the database.
            - None: If an error occurs during the database operation.
    '''

    print(f'Searching foia_data.db for "{search_string}"...')

    try:
        with sqlite3.connect('foia_data.db') as conn:

            results_table = pd.read_sql_query(check_results_table_query, conn)

            if results_table.empty:
                print('The `results` table does not exist in the database.')
                return None

            params = [f'%{search_string}%', f'%{search_string}%']

            df = pd.read_sql_query(search_foia_query, conn, params=params)

    except sqlite3.Error as e:
        print(f'Sqlite error: {e}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None

    return df


def parse_communications_column(communications) -> List[Dict]:
    '''
    Parses a communications column value, decoding it from JSON format.

    Args:
        communications : The input value to be parsed, which can be a JSON string or NaN.

    Returns:
        list (List[Dict]): A list containing the parsed JSON data. If the input is NaN (missing values) or
        there is a JSON decoding error, an empty list is returned.
    '''

    if pd.isna(communications):
        return []
    try:
        return json.loads(communications)
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON: {e}')
        return []


def generate_json(df: pd.DataFrame, search_string: str) -> None:
    '''
    Generates a JSON file from a pandas DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data to be written to the JSON file.

        search_string (str): The string used to name the output JSON file. Spaces in the string
            are replaced with underscores.

    Returns:
        None
    '''

    output_json = f'{search_string.replace(' ', '_')}.json'

    try:
        df.to_json(output_json, orient='records', indent=4)
        print(f'Matching entries written to "{output_json}"')
    except Exception as e:
        print(f'An error occurred while writing JSON: {e}')


def main() -> None:
    '''
    Function to search the foia_data.db database for entries matching a specified search string.

    Command Line Args:
        --search_for (str): A string to search for in the `title` and `tags` fields of FOIA requests.
    '''

    parser = parser_init()
    args = parser.parse_args()
    search_string = args.search_for

    if not os.path.exists('foia_data.db'):
        print('foia_data.db does not exist.\nRun create_foia_data_db.py first to create and populate it.')
        return

    df = search_foia_db(search_string)
    if df is None:
        return

    if not df['communications'].empty:
        df['communications'] = df['communications'].apply(
            parse_communications_column)

    print(f'Found {df.shape[0]} matching entries containing "{
          search_string}" in the title or tags')

    generate_json(df, search_string)


if __name__ == '__main__':
    main()
