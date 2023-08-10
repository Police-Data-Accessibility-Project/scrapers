import os

# filename = "./data/vehicle_ped_investigations/2020-present/2021_05_11_2020-present.csv"
# dir = "./"
def field_extractor(directory):
    """Extract fields from csv files in all sub directories of given directory."""
    fields = []

    for root, dirs, files in os.walk(directory):
        # print(files)
        for i in range(len(files)):
            if files[i].endswith(".csv"):
                filename = f"{root}/{files[i]}"
                # print(filename)
                f = open(filename, "r")
                try:
                    first_line = f.readline()
                except UnicodeDecodeError as exception:
                    print("Filename failed to decode: ", filename)
                    pass

                first_line_list = first_line.split(",")
                for i in range(len(first_line_list)):
                    if first_line_list[i] not in fields:
                        # print(first_line_list[i])
                        fields.append(first_line_list[i])

    with open("fields.txt", "a") as save_fields:
        for i in range(len(fields)):
            save_fields.write(f"* {fields[i]}\n")
