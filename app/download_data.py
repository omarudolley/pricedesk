import csv

import gdown
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

from app.constants import GOOGLE_DRIVE_PATH, LISTING_CSV_PATH, LISTING_JSON_PATH
from app.utils import read_from_file, save_as_json
from pathlib import Path


@retry(stop=stop_after_attempt(10), wait=wait_exponential(min=2, max=30))
def download_data_from_google_drive(url, output):
    logger.info("Downloading {url} to {dst}", url=url, dst=output)
    gdown.download(url, output, quiet=False)


def convert_csv_json_file(source, dest):
    temp = {}
    data = Path(source).open()
    csv_reader = csv.DictReader(data)

    for row in csv_reader:
        temp[row["Timestamp"]] = row

    print(temp)
    save_as_json(dest, temp)


def main():
    # Load data from external services
    logger.info("Downloading listing from google drive")
    download_data_from_google_drive(GOOGLE_DRIVE_PATH, LISTING_CSV_PATH + ".tmp")
    convert_csv_json_file(LISTING_CSV_PATH + ".tmp", LISTING_JSON_PATH)
