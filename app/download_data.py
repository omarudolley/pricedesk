import gdown
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

from app.constants import (
    LISTING_CSV_PATH,
    LISTING_ID,
)
from app.utils import analyze_time, analyze_memory
from app.helper import generate_google_drive_url


@retry(stop=stop_after_attempt(10), wait=wait_exponential(min=2, max=30))
def download_json_data(source, dest):
    gdown.download(source, dest, quiet=False)


@analyze_time
@analyze_memory
def main():
    # Load data from external services

    logger.info("Downloading listing from google drive")
    download_json_data(generate_google_drive_url(LISTING_ID), LISTING_CSV_PATH)
