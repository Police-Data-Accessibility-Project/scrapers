import camelot
import os
file_name = "apr-20"
directory = "./data/"
save_dir = "/csv/"


for root, dirs, files in os.walk(directory):
    if not os.path.exists(root + save_dir):
        print(" [*] Making save_dir")
        os.makedirs(root + save_dir)
    for name in files:
        # r.append(os.path.join(root, name))
        print(root, name)

    tables = camelot.read_pdf(root + os.sep + name, flavor='stream')

    tables.export(root + os.sep + save_dir + os.sep + name, f='csv', compress=False) # json, excel, html
    try:
        print(tables[0].parsing_report)
    except IndexError:
        print("No tables were found in " + root + os.sep + name)
        pass
    # tables[0].to_csv(file_name + ".csv") # to_json, to_excel, to_html
    # tables[0].df # get a pandas DataFrame!
