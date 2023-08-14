import tabula
import os
from tqdm import tqdm
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p) + "/utils")
from pdf_extraction.pdf_to_csv_cv import process_file

cur_dir = os.getcwd()
directory = cur_dir + "/data/"
folder = directory + "/tables/"


def save_file(file):
    print(file)
    # tables = tabula.read_pdf(directory + file, pages="all") # This loads the pdf into tabula
    tables = directory + file
    # print("Read")

    folder_name = folder + file.replace(".pdf", "/")


# Count number of files
pdf_count = 0
for file in os.listdir(directory):
    if file.endswith(".pdf"):
        pdf_count += 1
print("Total PDFS: " + str(pdf_count))


# read PDF file
print("Working... this may take a while")
for file in tqdm(os.listdir(directory), desc="Files", position=0, leave=True):
    if file.endswith(".pdf"):
        process_file(directory, file)
