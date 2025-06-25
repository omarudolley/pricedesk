from datetime import datetime
from datetime import timedelta
import pytz

GOOGLE_DRIVE_PATH_PREFIX = "https://docs.google.com/spreadsheets/d/"
GOOGLE_DRIVE_PATH_SUFFIX = "/export?exportFormat=csv"

LISTING_ID = "1CqjC08RQcXhC_Kg2sQEn03So9spvR_wuBIMzmukEsN0" 

LISTING_CSV_PATH = "data/listing.csv"

LIBERIA_TZ = pytz.timezone("GMT")

TODAY_DMYHM = datetime.today().astimezone(LIBERIA_TZ).strftime("%d/%m/%Y, %H:%M")
YESTERDAY_YMD = datetime.strftime(datetime.today() - timedelta(1), "%Y-%m-%d")


STATS_BAR_LRD_PATH = "frontend/src/lib/data/stats/lrd/StatsBar.json"
STATS_BAR_USD_PATH = "frontend/src/lib/data/stats/usd/StatsBar.json"

MAP_DATA_LRD_PATH = "frontend/src/lib/data/map/lrd/Map.json"
MAP_DATA_USD_PATH = "frontend/src/lib/data/map/usd/Map.json"

INFLATION_DATA_PATH = "frontend/src/lib/data/inflation/data.json"

COMMODITY_LIST = [
    "USD buying rate",
    "USD selling rate",
    "Corned Beef (carton)",
    "Loaf of bread (Fula)",
    "Loaf of bread (Round)",
    "Cement (bag)",
    "Charcoal (bag)",
    "Diesel (gallon)",
    "Gasoline (gallon)",
    "Eggs(cart)",
    "Eggs (carton)",
    "Garri (bucket)",
    "Garri (bag)",
    "Garri (cup)",
    "Milk (tin)",
    "Milk (carton)",
    "Palm oil (500ml)",
    "Palm oil (1.5L)",
    "Palm oil (gallon)",
    "Palm oil (tin)",
    "Vegetable oil (500ml)",
    "Vegetable oil (1.5L)",
    "Vegetable oil (gallon)",
    "Vegetable oil (tin)",
    "Rice (25kg)",
    "Rice (50kg)",
    "Rice (cup)",
    "Sugar (cup)",
    "Sugar (bucket)",
    "Sugar (bag)",
    "Water bottle (500ml)",
    "Water bottle (1.5L)",
    "Water (sack)",
    "Crush rock (blade)",
    "Steel rod (single)",
    "Roofing Zinc (sheet)",
    "Roofing Zinc (bundle)",
    "Oil Paint (gallon)",
    "Oil Paint (bucket)",
    "Water Paint (gallon)",
    "Water Paint (bucket)",
    "Whitewash (bag)",
    "Brick (4-inch)",
    "Brick (6-inch)",
    "Brick (8-inch)",
    "Roofing nail (box)",
    'Plank (2" by 2")',
    'Plank (2" by 4")',
    'Plank (2" by 6")',
    "Round pole (single)",
    "Beach Sand (blade)",
    "Corned Beef (1 can)",
    "Beef(Ibs)",
    "Onions(bag)",
    "Cube Magi(pk)",
    "Flour(bag)",
]


LOCATION = [
    "Gbapolu",
    "Bong",
    "Grand Bassa",
    "Grand Cape Mount",
    "Lofa",
    "Montserrado",
    "Margibi",
    "Nimba",
    "Rivercess",
    "Grand Gedeh",
    "Sinoe",
    "River Gee",
    "Grand Kru",
    "Maryland",
    "Bomi",
]
