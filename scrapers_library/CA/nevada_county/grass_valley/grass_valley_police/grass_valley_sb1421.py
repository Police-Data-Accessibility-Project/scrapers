import sys
import os

import requests
from tqdm import tqdm
from vimeo_downloader import Vimeo
from from_root import from_root

p = from_root("CONTRIBUTING.md").parent
sys.path.insert(1, str(p))

from utils.pdf.list_pdf_scrapers.single_pdf_scraper import single_pdf_scraper


def get_sharepoint_pdfs():
    """Downloads PDF files that are hosted on Microsoft SharePoint."""    
    pdfs = [
        {
            "name": "Grass Valley Police Incident Report.pdf",
            "url1": "https://cityofgrassvalley-my.sharepoint.com/%3Ab%3A/g/personal/bkalstein_gvpd_net/EX1xjYG48R1Nk-vaAX9HOJYBlIjjKO13gKZLdXzkHOv0SQ?e=2lfUg1",
            "url2": "https://cityofgrassvalley-my.sharepoint.com/personal/bkalstein_gvpd_net/Documents/GVPD/OIS/Open%20Access/Grass%20Valley%20Police%20Incident%20Report.pdf"
        },
        {
            "name": "Internal Review and Findings.pdf",
            "url1": "https://cityofgrassvalley-my.sharepoint.com/%3Ab%3A/g/personal/bkalstein_gvpd_net/EaVFsdEin1FMiUaf8SklOoAB51Bt8shEF376SWVHrgUgXA?e=RDd9VP",
            "url2": "https://cityofgrassvalley-my.sharepoint.com/personal/bkalstein_gvpd_net/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fbkalstein%5Fgvpd%5Fnet%2FDocuments%2FGVPD%2FOIS%2FOpen%20Access%2FInternal%20Review%20and%20Findings%2Epdf"
        },
        {
            "name": "District Attorney Findings and Report of Incident.pdf",
            "url1": "https://cityofgrassvalley-my.sharepoint.com/%3Ab%3A/g/personal/bkalstein_gvpd_net/Efx7ivUAGwVKiQYbt8S4dtYBLqcxTwdt52fhjNvOHVRmPQ?e=dGZBnD",
            "url2": "https://cityofgrassvalley-my.sharepoint.com/personal/bkalstein_gvpd_net/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fbkalstein%5Fgvpd%5Fnet%2FDocuments%2FGVPD%2FOIS%2FOpen%20Access%2FDA%5Freview%5Fstrickland%2Epdf"
        }
    ]

    print("\nRetrieving Sharpoint PDFs...")
    for pdf in pdfs:
        filepath = "./data/G2000004/" + pdf["name"]

        if os.path.exists(filepath):
            continue

        # Perform a get request to the first url to retrieve a FedAuth cookie for download authorization
        res = requests.get(pdf["url1"])
        cookie_dict = res.cookies.get_dict()
        headers = {"Cookie": f"FedAuth={cookie_dict['FedAuth']}"}
        
        res = requests.get(pdf["url2"], headers=headers, stream=True)
        total = int(res.headers.get('content-length', 0))
        progress_bar = tqdm(total=total, unit='iB', unit_scale=True, desc=pdf["name"])

        with open(filepath, "wb") as fd:
            for chunk in res.iter_content(chunk_size=1024):
                progress_bar.update(len(chunk))
                fd.write(chunk)
        
        progress_bar.close()


def get_vimeo_videos():
    """Downloads videos that are hosted on Vimeo."""
    embedded_on = "https://www.cityofgrassvalley.com/"
    videos = [
        {
            "dir": "./data/G2000004",
            "url": "https://player.vimeo.com/video/395570204"
        },
        {
            "dir": "./data/G2000004",
            "url": "https://player.vimeo.com/video/394047232"
        },
        {
            "dir": "./data/G2000004",
            "url": "https://player.vimeo.com/video/394046683"
        },
        {
            "dir": "./data/G2000004",
            "url": "https://player.vimeo.com/video/394048251"
        },
        {
            "dir": "./data/G2000004",
            "url": "https://player.vimeo.com/video/685656476"
        },
        {
            "dir": "./data/G1901078",
            "url": "https://player.vimeo.com/video/702224442"
        },
        {
            "dir": "./data/G1901078",
            "url": "https://player.vimeo.com/video/702221548"
        }
    ]

    print("\nRetrieving video files...")
    for video in videos:
        v = Vimeo(video["url"], embedded_on)
        stream = v.streams

        if os.path.exists(f"{video['dir']}/{stream[-1].title}.mp4"):
            continue
        
        stream[-1].download(download_directory=video["dir"])


def main():
    pdfs = [
        {
            "dir": "./data/G2300034/",
            "url": "https://www.cityofgrassvalley.com/sites/main/files/file-attachments/g2300034_-_incident_report.pdf"
        },
        {
            "dir": "./data/G1901078/",
            "url": "https://www.cityofgrassvalley.com/sites/main/files/file-attachments/g1901078_ir_redacted.pdf"
        }
    ]

    for pdf in pdfs:
        single_pdf_scraper(pdf["dir"], pdf["url"])

    if not os.path.exists("./data/G2000004/"):
        os.makedirs("./data/G2000004/")

    get_sharepoint_pdfs()

    get_vimeo_videos()


if __name__ == "__main__":
    main()
