import sqlite3
import pandas as pd
import json
import argparse


def parse_communications_column(communications):
    if pd.isna(communications):
        return []
    try:
        return json.loads(communications)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []


def search_foia_db(search_string):
    print(f"'Searching foia_data.db for '{search_string}'...")

    try:
        with sqlite3.connect('foia_data.db') as conn:
            query = '''
                SELECT * FROM results
                WHERE (title LIKE ? OR tags LIKE ?)
                AND (status = 'done')
                '''
            params = [f'%{search_string}%', f'%{search_string}%']

            df = pd.read_sql_query(query, conn, params=params)

    except sqlite3.Error as e:
        print(f'Sqlite error: {e}')
        return None

    return df


def generate_json(df, search_string):
    output_json = f"{search_string.replace(' ', '_')}.json"

    df.to_json(output_json, orient='records', indent=4)

    print(f"Matching entries written to '{output_json}'")


def main():
    parser = argparse.ArgumentParser(
        description="Search foia_data.db and generate JSON file of resulting matches")
    parser.add_argument('--search_for', type=str, required=True,
                        help="Provide a string to search foia_data.db")

    args = parser.parse_args()
    search_string = args.search_for

    df = search_foia_db(search_string)
    if df is None:
        return

    df['communications'] = df['communications'].apply(
        parse_communications_column)

    print(f"Found {df.shape[0]} matching entries containing '{
          search_string}' in the title or tags")

    generate_json(df, search_string)


if __name__ == '__main__':
    main()
