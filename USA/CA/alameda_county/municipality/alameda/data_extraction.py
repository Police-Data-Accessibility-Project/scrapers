import camelot
import os
file_name = "apr-20"
directory = "./data/"
save_dir = "/csv/"


for root, dirs, files in os.walk(dir):
    for name in files:
        # r.append(os.path.join(root, name))
        print(root, name)

    tables = camelot.read_pdf(directory + file_name + ".pdf", flavor='stream')

    tables.export(root + save_dir + file_name, f='csv', compress=False) # json, excel, html
    print(tables[0].parsing_report)
    # tables[0].to_csv(file_name + ".csv") # to_json, to_excel, to_html
    # tables[0].df # get a pandas DataFrame!
