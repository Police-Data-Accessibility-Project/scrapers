import os

# filename = "./data/vehicle_ped_investigations/2020-present/2021_05_11_2020-present.csv"
dir  = "./"
for root, dirs, files in os.walk(dir):
    print(files)
    # print(files)
    for i in range(len(files)):
        if files[i].endswith(".csv"):
            filename = f"{root}/{files[i]}"
            print(filename)
            f = open(filename, "a+")
            read_file = f.read()
            if "TRUNCATED" not in read_file:
                f.truncate(930)
                f.write("\nTRUNCATED")
                f.close()
