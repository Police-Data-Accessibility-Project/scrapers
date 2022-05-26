# PDAP-Scraper-Setup-GUI
A local Python GUI to help you write data scrapers. Our latest releases are [here]([url](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/releases)).

# Usage:
Follow the instructions in [`CONTRIBUTING.md`](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/blob/main/CONTRIBUTING.md).

If you only want to create a scraper, you can install the bare minimum requirements for the creation gui by running:
(from the PDAP-Scrapers folder)
```
cd setup_gui
```
```
python3 -m pip install -r min_requirements.txt
```

If you plan on contributing more/running a scraper, install the full requirements from [here](https://github.com/Police-Data-Accessibility-Project/PDAP-Scrapers/blob/main/requirements.txt)

# Building
1. Install `pyinstaller`
```
pip install pyinstaller
```
2. Run
```
pyinstaller --onefile --windowed --console ScraperSetup.py
```
