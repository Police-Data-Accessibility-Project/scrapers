import requests
from bs4 import BeautifulSoup
import csv
import re

# URL of the page to scrape
url = "https://www.alleghenycounty.us/Government/Police-and-Emergency-Services/Police/More-Information/Police-Departments-by-Municipality"

# Fetch the page
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

# Find all tables containing the police departments
tables = soup.find_all("table", {"class": "sc-responsive-table"})

# Lists to store the data
departments_data = []
no_department_data = []

# Function to clean the text and improve formatting
def clean_text(text):
    text = text.replace('\n', ' ').replace('\r', ' ')
    text = re.sub(' +', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()

# Iterate through each table and process the rows
for table in tables:
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")
    for row in rows:
        # Get all three columns data
        columns = row.find_all("td")
        name = clean_text(columns[0].get_text())
        contact_info = clean_text(columns[1].get_text())
        jurisdictions_covered = clean_text(columns[2].get_text())
        
        if "No Police Department" in name:
            no_department_data.append([name, contact_info, jurisdictions_covered])
        else:
            departments_data.append([name, contact_info, jurisdictions_covered])

# Write the data to CSV files
csv_filename_departments = "police_departments.csv"
csv_filename_no_departments = "no_police_departments.csv"

# Save police departments data
with open(csv_filename_departments, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Contact Info", "Jurisdictions Covered"])
    writer.writerows(departments_data)

# Save no police departments data
with open(csv_filename_no_departments, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Contact Info", "Jurisdictions Covered"])
    writer.writerows(no_department_data)

# Print summary
print(f"Total number of police departments: {len(departments_data)}")
print(f"CSV file '{csv_filename_departments}' has been saved.")
print(f"Total number of 'No Police Department' entries: {len(no_department_data)}")
print(f"CSV file '{csv_filename_no_departments}' has been saved.")
