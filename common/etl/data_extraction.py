import camelot
import os

# pdf_directory = "./data/"
# save_dir = "/csv/"

def pdf_extract(pdf_directory="./data/", csv_dir="/csv/", delete_pdf=False, flavor="stream"):
    """
    Test implementation of camelot's pdf extraction
    :param pdf_directory: parent directory of pdf folder(s) (default "./data/")
    :param csv_dir: where csv result will be saved. appended to root directory. (default "./data/")
    :param delete_pdf: whether to delete the pdf when done. best to leave false (default False)
    :param flavor: camelot extraction flavor, either "stream" or "lattice". (default "stream")
    """
    
    for root, dirs, files in os.walk(pdf_directory):
        if "csv" not in root:
            if not os.path.exists(root + csv_dir):
                print(" [*] Making csv_dir... \n")
                os.makedirs(root + csv_dir)
        for name in files:
            # r.append(os.path.join(root, name))
            print(f"  [*] Extracting: {root}{os.sep}{name}")
            if "csv" not in root:
                print(" [*] Reading pdf: " + name)
                tables = camelot.read_pdf(root + os.sep + name, flavor=flavor)
                print("    [*] Exporting tables to: " + root + os.sep + csv_dir)
                tables.export(root + os.sep + csv_dir + os.sep + name.strip(".pdf") + ".csv", f='csv', compress=False) # json, excel, html
                try:
                    print(f"    [STATS] {tables[0].parsing_report}")
                except IndexError:
                    print("    [!] No tables were found in " + root + os.sep + name)
                    pass
                # tables[0].to_csv(file_name + ".csv") # to_json, to_excel, to_html
                # tables[0].df # get a pandas DataFrame!
