import json

url_table = [
    "https://lky-open-data.s3.amazonaws.com/LMPD/LMPD_OP_BIAS.csv",
    "https://lky-open-data.s3.amazonaws.com/LMPD/AssaultedOfficerData.csv",
    "https://data.louisvilleky.gov/sites/default/files/27091/Crime_Data_2019.csv",
    "https://lky-open-data.s3.amazonaws.com/LMPD/LMPD_Demographics.csv",
    "https://data.louisvilleky.gov/sites/default/files/UniformCitationData%20.csv",
    "https://lky-open-data.s3.amazonaws.com/LMPD/LMPD_STOPS_DATA.CSV",
    "https://data.louisvilleky.gov/sites/default/files/Firearm%20Data_normalized_addresses.csv",
    "https://data.louisvilleky.gov/sites/default/files/fiream_data_intersections_reprocessed.csv",
]

# Change to what you need (remove what you don't)
save_table = [
    "hate_crimes/",
    "assaulted_officers/",
    "crime_data/",
    "employee_characteristics/",
    "uniform_citation_data/",
    "stops_data/",
    "firearm_intake/normalized_addresses/",
    "firearm_intake/intersections/",
]

# url_save = [
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
#     [save_folder, url],
# ]

url_save = []
for i, row in enumerate(url_table):
    updated_table = [save_table[i], url_table[i]]
    url_save.append(updated_table)

with open("updated_table.txt", "a") as output:
    output.write(f"save_url = {json.dumps(url_save, indent=4)}")
