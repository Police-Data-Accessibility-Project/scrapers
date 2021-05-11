import os

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

filename = "./data/vehicle_ped_investigations/2020-present/2021_05_11_2020-present.csv"

for root, dirs, files in os.walk(dir):
    if ".csv" in files:
        filename = root + files
        f = open(filename, "a")
        read_file = f.read()
        if "TRUNCATED" not in read_file:
            f.truncate(930)
            f.write("\nTRUNCATED")
            f.close()
