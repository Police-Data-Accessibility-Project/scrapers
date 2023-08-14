import os


def field_extractor(directory):
    """Extract fields from csv files in all sub directories of given directory."""
    fields = []

    for root, dirs, files in os.walk(directory):
        for i in range(len(files)):
            if files[i].endswith(".csv"):
                filename = f"{root}/{files[i]}"
                f = open(filename, "r")
                try:
                    first_line = f.readline()
                except UnicodeDecodeError as exception:
                    print("Filename failed to decode: ", filename)
                    pass

                first_line_list = first_line.split(",")
                for i in range(len(first_line_list)):
                    if first_line_list[i] not in fields:
                        fields.append(first_line_list[i])

    with open("fields.txt", "a") as save_fields:
        for i in range(len(fields)):
            save_fields.write(f"* {fields[i]}\n")
