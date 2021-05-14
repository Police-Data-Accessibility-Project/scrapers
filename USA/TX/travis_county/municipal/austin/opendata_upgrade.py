url_table = [
    "https://data.austintexas.gov/resource/fdj4-gpfu.csv",
    "https://data.austintexas.gov/resource/4bxg-n3iv.csv",
    "https://data.austintexas.gov/resource/dmxv-zsfa.csv",
    "https://data.austintexas.gov/resource/9dis-d5bk.csv",
    "https://data.austintexas.gov/resource/87wz-a3h2.csv",
    "https://data.austintexas.gov/resource/gzfe-bzj4.csv",
]

# Change to what you need (remove what you don't)
save_table = [
    "crime_reports/",
    "crime_reports/2017/",
    "hate_crimes/2021/",
    "racial_profiling/motor_vehicle_stops/",
    "population_vs_MV_stops/",
    "warning_obs/",
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

print(url_save)
