# PDAP-Scraper-Setup-GUI
A local Python GUI to help you write data scrapers.

# Usage:

1. Clone this repository. Don't know how? See [Creating Cloning and Archiving Repositories](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
2. Clone our [scraper repo][https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/]
3. Follow through the GUI. You can either run the script directly `python3 scraper_setup.py`, or run the executable by double clicking it.
4. Copy the resulting folder into your clone of `PDAP-Scrapers`
5. Open a Pull Request on GitHub for PDAP-Scrapers.

## Script Usage

1. Install dependencies. `pip install -r requirements.txt`

## Build
1. Install `pyinstaller`
```
pip install pyinstaller
```
2. Run
```
pyinstaller --onefile --windowed --console scraper_setup.py
```
