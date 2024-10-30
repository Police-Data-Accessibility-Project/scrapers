import requests
import pandas as pd
import sqlite3
import logging
import os
import json
import time
from typing import List, Tuple, Dict, Any, Union

logging.basicConfig(filename='errors.log', level=logging.ERROR,
                    format='%(levelname)s: %(message)s')


base_url = 'https://www.muckrock.com/api_v1/foia/'
last_page_fetched = 'last_page_fetched.txt'

NO_MORE_DATA = -1  # flag for program exit
JSON = Dict[str, Any]  # type alias


create_table_query = '''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                title TEXT,
                slug TEXT,
                status TEXT,
                embargo_status TEXT,
                user INTEGER,
                username TEXT,
                agency INTEGER,
                datetime_submitted TEXT,
                date_due TEXT,
                days_until_due INTEGER,
                date_followup TEXT,
                datetime_done TEXT,
                datetime_updated TEXT,
                date_embargo TEXT,
                tracking_id TEXT,
                price TEXT,
                disable_autofollowups BOOLEAN,
                tags TEXT,
                communications TEXT,
                absolute_url TEXT
            )
            '''


foia_insert_query = '''
        INSERT INTO results (id, title, slug, status, embargo_status, user, username, agency,
                            datetime_submitted, date_due, days_until_due, date_followup,
                            datetime_done, datetime_updated, date_embargo, tracking_id,
                            price, disable_autofollowups, tags, communications, absolute_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''


def create_db() -> None:
    '''
    Creates foia_data.db SQLite database with one table named `results`.

    Returns:
        None
    '''

    try:
        with sqlite3.connect('foia_data.db') as conn:
            conn.execute(create_table_query)
            conn.commit()
        print('Successfully created foia_data.db!')
    except sqlite3.Error as e:
        print(f'SQLite error: {e}.')


def fetch_page(page: int) -> Union[JSON, NO_MORE_DATA, None]:
    '''
    Fetches a page of 100 results from the MuckRock FOIA API.

    Args:
        page (int): The page number to fetch from the API.

    Returns:
        Union[JSON, None, NO_MORE_DATA]:
            - JSON Dict[str, Any]: The response's JSON data, if the request is successful.
            - NO_MORE_DATA (int): A constant, if there are no more pages to fetch (indicated by a 404 response).
            - None: If there is an error other than 404.
    '''

    per_page = 100
    response = requests.get(
        base_url, params={'page': page, 'page_size': per_page, 'format': 'json'})

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print('No more pages to fetch')
        return NO_MORE_DATA  # Typically 404 response will mean there are no more pages to fetch
    elif 500 <= response.status_code < 600:
        logging.error(f'Server error {response.status_code} on page {page}')
        page = page + 1
        return fetch_page(page)
    else:
        print(f'Error fetching page {page}: {response.status_code}')
        logging.error(f'Fetching page {page} failed with response code: {
                      response.status_code}')
        return None


def transform_page_data(data_to_transform: JSON) -> List[Tuple[Any, ...]]:
    '''
    Transforms the data recieved from the MuckRock FOIA API into a structured format for insertion into a database with `populate_db()`.

    Transforms JSON input into a list of tuples, as well as serializes the nested `tags` and `communications` fields into JSON strings.

    Args:
        data_to_transform (JSON: Dict[str, Any]): The JSON data from the API response.

    Returns:
        transformed_data (List[Tuple[Any, ...]]: A list of tuples, where each tuple contains the fields of a single FOIA request.
    '''

    transformed_data = []

    for result in data_to_transform.get('results', []):
        result['tags'] = json.dumps(result.get('tags', []))
        result['communications'] = json.dumps(
            result.get('communications', []))

        transformed_data.append((
            result['id'],
            result['title'],
            result['slug'],
            result['status'],
            result['embargo_status'],
            result['user'],
            result['username'],
            result['agency'],
            result['datetime_submitted'],
            result['date_due'],
            result['days_until_due'],
            result['date_followup'],
            result['datetime_done'],
            result['datetime_updated'],
            result['date_embargo'],
            result['tracking_id'],
            result['price'],
            result['disable_autofollowups'],
            result['tags'],
            result['communications'],
            result['absolute_url']
        ))
    return transformed_data


def populate_db(transformed_data: List[Tuple[Any, ...]]) -> None:
    '''
    Populates foia_data.db SQLite database with the transfomed FOIA request data.

    Args:
        transformed_data (List[Tuple[Any, ...]]): A list of tuples, where each tuple contains the fields of a single FOIA request.

    Returns:
        None
    '''

    with sqlite3.connect('foia_data.db') as conn:

        retries = 0
        max_retries = 2
        while retries < max_retries:
            try:
                conn.executemany(foia_insert_query, transformed_data)
                conn.commit()
                print('Successfully inserted data!')
                return
            except sqlite3.Error as e:
                print(f'SQLite error: {e}. Retrying...')
                conn.rollback()
                retries += 1
                time.sleep(1)

        if retries == max_retries:
            print(f'Failed to insert data from page {page} after {
                max_retries} attempts. Skipping to next page.')
            logging.error(f'Failed to insert data from page {page} after {
                max_retries} attempts.')


def main() -> None:
    '''
    Main entry point for create_foia_data_db.py.

    This function orchestrates the process of fetching FOIA requests data from the MuckRock FOIA API, transforming it,
    and storing it in a SQLite database.
    '''

    if not os.path.exists('foia_data.db'):
        print('Creating foia_data.db...')
        try:
            create_db()
        except:
            print('Failed to create foia_data.db')
            return

    if os.path.exists(last_page_fetched):
        with open(last_page_fetched, mode='r') as file:
            page = int(file.read()) + 1
    else:
        page = 1

    while True:

        print(f'Fetching page {page}...')
        page_data = fetch_page(page)

        if page_data == NO_MORE_DATA:
            break  # Exit program no more data exixts
        if page_data is None:
            print(f'Skipping page {page}...')
            page += 1
            continue

        transformed_data = transform_page_data(page_data)

        populate_db(transformed_data)

        with open(last_page_fetched, mode='w') as file:
            file.write(str(page))
        page += 1

    print('create_foia_data_db.py run finished')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        print('Check errors.log to review errors. Run make_foia_db.py again to continue')
