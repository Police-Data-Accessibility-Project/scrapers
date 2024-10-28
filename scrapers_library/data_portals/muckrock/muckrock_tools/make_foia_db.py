import requests
import csv
import time
import json
import pandas as pd
import sqlite3
import logging
import os

logging.basicConfig(filename='errors.log', level=logging.ERROR,
                    format='%(levelname)s: %(message)s')


base_url = 'https://www.muckrock.com/api_v1/foia/'
page = 1
per_page = 100
last_page_fetched = 'last_page_fetched.txt'
max_retries = 2


def fetch_page(page):
    response = requests.get(
        base_url, params={'page': page, 'page_size': per_page, 'format': 'json'})
    print("headers: ", response.request.headers, 'text: ', response.text)
    if response.status_code == 200:
        return response.json()
    elif 500 <= response.status_code < 600:
        logging.error(f'Server error {response.status_code} on page {page}')
        time.sleep(5)
        return fetch_page(page)
    else:
        print(f'Error fetching page {page}: {response.status_code}')
        logging.error(f'Fetching page {page} failed with response code: {
                      response.status_code}')
        return None


def make_foia_db(page):

    with sqlite3.connect('foia_data.db') as conn:

        conn.execute('''
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
                communications TEXT
            )
            ''')

        insert_foia = '''
                    INSERT INTO results (id, title, slug, status, embargo_status, user, username, agency,
                                        datetime_submitted, date_due, days_until_due, date_followup,
                                        datetime_done, datetime_updated, date_embargo, tracking_id,
                                        price, disable_autofollowups, tags, communications)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    '''

        if os.path.exists(last_page_fetched):
            with open(last_page_fetched, mode='r') as file:
                page = int(file.read()) + 1

        while True:
            print(f'Fetching page {page}...')
            data = fetch_page(page)
            if data is None:
                print(f'Skipping page {page}...')
                page += 1
                continue

            all_data = []
            for result in data.get('results', []):
                result['tags'] = json.dumps(result.get('tags', []))
                result['communications'] = json.dumps(
                    result.get('communications', []))

                all_data.append((
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
                    result['communications']
                ))

            retries = 0
            while retries < max_retries:
                try:
                    conn.executemany(insert_foia, all_data)
                    conn.commit()
                    break
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
                with open(last_page_fetched, mode='w') as file:
                    file.write(str(page))
                page += 1
                continue

            if not data.get('next'):
                break

            with open(last_page_fetched, mode='w') as file:
                file.write(str(page))

            page += 1

    print('Data fetching and insertion complete.')


if __name__ == '__main__':
    try:
        make_foia_db(page)
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        print('Run make_foia_db.py again to continue')
