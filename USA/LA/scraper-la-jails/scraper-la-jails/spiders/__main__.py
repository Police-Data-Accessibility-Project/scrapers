from scrape_la_jails import run_scraper
import os


def main():
    print(os.getcwd())
    print("Starting scraper for LA jails")
    print(run_scraper())
    print("Done")


if __name__ == "__main__":
    main()
