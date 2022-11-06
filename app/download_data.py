import csv

import gdown
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

from app.constants import GOOGLE_DRIVE_PATH, LISTING_JSON_PATH
from app.utils import save_as_json, analyze_time, analyze_memory
from pathlib import Path
from tempfile import NamedTemporaryFile


@retry(stop=stop_after_attempt(10), wait=wait_exponential(min=2, max=30))
def download_json_data(source, dest):
    with NamedTemporaryFile() as f:
        logger.info("Downloading {url} to {dst}", url=GOOGLE_DRIVE_PATH, dst=f.name)
        gdown.download(source, f.name, quiet=False)

        data = Path(f.name).open()
        csv_reader = csv.DictReader(data)
        data_dict = {}

        for row in csv_reader:
            data_dict[row["Timestamp"]] = row

        save_as_json(dest, data_dict)


@analyze_time
@analyze_memory
def main():
    # Load data from external services
    logger.info("Downloading data from google drive")

    download_json_data(GOOGLE_DRIVE_PATH, LISTING_JSON_PATH)
