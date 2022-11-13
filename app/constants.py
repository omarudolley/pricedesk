from datetime import datetime
from datetime import timedelta
import pytz

GOOGLE_DRIVE_PATH_PREFIX = "https://docs.google.com/spreadsheets/d/"
GOOGLE_DRIVE_PATH_SUFFIX = "/export?exportFormat=csv"

DUALA_LISTING_ID = "183aea1tYahSyjfz4Xhgxy03tBlRLNz20IvOlwezxOAo"
RED_LIGHT_LISTING_ID = "1Ozxrw0kn0fvWgWyem0OAyvdmivrkzAl_s630UEbhc04"
WATERSIDE_LISTING_ID = "1_jXGlI-T3rRH68fJ7esxO9AXOD82-PklFwcmnJpZSRA"

RED_LIGHT_LISTING_CSV_PATH = "data/raw/redlight.csv"
DUALA_LISTING_CSV_PATH = "data/raw/duala.csv"
WATERSIDE_LISTING_CSV_PATH = "data/raw/waterside.csv"

RAW_DATA_PATH = "data/raw/"

LIBERIA_TZ = pytz.timezone("GMT")

TODAY_DMYHM = datetime.today().astimezone(LIBERIA_TZ).strftime("%d/%m/%Y, %H:%M")
YESTERDAY_YMD = datetime.strftime(datetime.today() - timedelta(1), "%Y-%m-%d")


STATS_BAR_LRD_PATH = "frontend/src/lib/data/stats/lrd/StatsBar.json"
STATS_BAR_USD_PATH = "frontend/src/lib/data/stats/usd/StatsBar.json"

COMMODITY_LIST = [
    "Rice",
    "Gasoline",
    "Diesel",
    "Charcoal",
    "Palm oil",
    "Vegetable oil",
    "Beef",
    "Sugar",
    "Eggs",
    "Water sack",
    "Cement",
    "USD buying rate",
    "USD selling rate",
    "Bread",
    "Milk",
    "Garri",
    "Water bottle",
]
