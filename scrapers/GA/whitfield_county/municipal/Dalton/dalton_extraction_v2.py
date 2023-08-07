import tabula
import os

cur_dir = os.getcwd()
directory = cur_dir + r"\data\\"
folder = cur_dir + r"\tables\\"
traffic = folder + r"\traffic\\"
crime = folder + r"\crime\\"

# Checks if folder exists and creates it
if not os.path.isdir(folder):
    print("Making folder")
    os.makedirs(folder)
if not os.path.isdir(traffic):
    os.makedirs(traffic)
if not os.path.isdir(crime):
    os.makedirs(crime)


def save_file(file):
    print(file)
    tables = tabula.read_pdf(
        directory + file, pages="all"
    )  # Reads the pdf using tabula
    print("read")
    if "crime" in file.lower():
        folder_name = crime + file.replace(".pdf", "\\")
    elif "traffic" in file.lower() or "crash" in file.lower():
        folder_name = traffic + file.replace(".pdf", "\\")
    else:
        folder_name = folder + file.replace(
            ".pdf", "\\"
        )  # Replaces the file extension with \
    print(folder_name)
    # save them in a folder
    if not os.path.isdir(folder_name):
        print("Making folder")
        os.makedirs(folder_name)
    # iterate over extracted tables and export as excel individually
    for i, table in enumerate(tables, start=1):
        table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)


# read PDF file
for file in os.listdir(directory):
    save_file(file)
