url_table = [
    "https://data.cityofnewyork.us/api/views/5uac-w243/rows.csv?accessType=DOWNLOAD",
    "https://data.cityofnewyork.us/api/views/57mv-nv28/rows.csv?accessType=DOWNLOAD",
]

# Change to what you need (remove what you don't)
save_table = [
    "crime_data/",  # called "complaints" on website
    "crime_data/historic",
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
    output.write(f"save_url = {url_save}")
