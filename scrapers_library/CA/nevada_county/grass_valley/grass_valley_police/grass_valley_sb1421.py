import sys

import requests
from vimeo_downloader import Vimeo
from from_root import from_root

p = from_root("CONTRIBUTING.md").parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers.single_pdf_scraper import single_pdf_scraper

'''
url = "https://player.vimeo.com/video/702224442"
embedded_on = 'https://www.cityofgrassvalley.com/post/g1901078'
v = Vimeo(url, embedded_on)
stream = v.streams
stream[-1].download(download_directory='./test', filename='test5')
'''

'''
file_url = "https://cityofgrassvalley-my.sharepoint.com/%3Ab%3A/g/personal/bkalstein_gvpd_net/EaVFsdEin1FMiUaf8SklOoAB51Bt8shEF376SWVHrgUgXA?e=RDd9VP"
save_path = './data/G2000004/'

res = requests.get(file_url)
cookie_dict = res.cookies.get_dict()
file_url = 'https://cityofgrassvalley-my.sharepoint.com/personal/bkalstein_gvpd_net/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fbkalstein%5Fgvpd%5Fnet%2FDocuments%2FGVPD%2FOIS%2FOpen%20Access%2FInternal%20Review%20and%20Findings%2Epdf'
headers = {"Cookie": f"FedAuth={cookie_dict['FedAuth']}"}
res = requests.get(file_url, headers=headers)
print(res)
file_path = "./data/G2000004/test.pdf"
with open(file_path, "wb") as fd:
    for chunk in res.iter_content():
        fd.write(chunk)

'''

def get_vimeo_videos():
    videos = [
        [
            ""
        ]
    ]


def main():
    pdfs = [
        {
            "save_dir": "./data/G2300034/",
            "url": "https://www.cityofgrassvalley.com/sites/main/files/file-attachments/g2300034_-_incident_report.pdf"
        },
        {
            "save_dir": "./data/G1901078/",
            "url": "https://www.cityofgrassvalley.com/sites/main/files/file-attachments/g1901078_ir_redacted.pdf"
        }
    ]

    for pdf in pdfs:
        single_pdf_scraper(pdf["save_dir"], pdf["url"])
    
    get_vimeo_videos()


if __name__ == "__main__":
    main()
