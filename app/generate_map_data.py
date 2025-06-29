from app.utils import analyze_memory
from app.utils import analyze_time
from app.utils import logger
from app.utils import save_as_json
from app.helper import generate_in_usd, average_values_for_montserrado

import pandas as pd
import numpy as np
from datetime import datetime
import pytz
from app.constants import (
    LISTING_CSV_PATH,
    MAP_DATA_USD_PATH,
    MAP_DATA_LRD_PATH,
    COMMODITY_LIST,
    LOCATION,
    TODAY_DMYHM,
)

LOCAL_TZ = pytz.timezone("Africa/Monrovia")
TODAY_DMYHM = datetime.now(LOCAL_TZ).strftime("%d/%m/%Y %H:%M")


def parse_dates_column(df):
    """Parse 'Date' column as datetime using DD/MM/YYYY format, localize to Monrovia."""
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    df.dropna(subset=["Date"], inplace=True)

    # Normalize time to midnight and convert to timezone
    df["Date"] = df["Date"].dt.tz_localize("UTC").dt.tz_convert(LOCAL_TZ)
    df["Date"] = df["Date"].dt.strftime("%d/%m/%Y")  # Convert back to string for output keys
    return df


@analyze_time
@analyze_memory
def main():
    logger.info("Loading local data files")
    df = pd.read_csv(LISTING_CSV_PATH)

   # Drop optional column
    df.drop("Timestamp", inplace=True, axis=1, errors="ignore")

    # Parse date column and localize timezone
    df = parse_dates_column(df)

    # Extract and sort unique formatted dates
    dates = sorted(set(df["Date"]))

    # Process raw and USD data
    df_avg = average_values_for_montserrado(df, dates)
    df_usd = generate_in_usd(df_avg)

    df_avg = df_avg.round(0)
    df_usd = df_usd.round(2)

    # Set multi-index
    df_avg.set_index(["Date", "Location"], inplace=True)
    df_usd.set_index(["Date", "Location"], inplace=True)

    # Convert to lookup dicts
    df_avg_dict = df_avg.to_dict()
    df_usd_dict = df_usd.to_dict()

    # Prepare output
    final_ld_data = {"dates": dates, "updatedOn": TODAY_DMYHM}
    final_usd_data = {"dates": dates, "updatedOn": TODAY_DMYHM}

    for item in COMMODITY_LIST:
        final_ld_data[item] = [
            {"date": d, "data": [[df_avg_dict[item].get((d, loc))] for loc in LOCATION]}
            for d in dates
        ]
        final_usd_data[item] = [
            {"date": d, "data": [[df_usd_dict[item].get((d, loc))] for loc in LOCATION]}
            for d in dates
        ]
    save_as_json(MAP_DATA_USD_PATH, final_usd_data)
    save_as_json(MAP_DATA_LRD_PATH, final_ld_data)


if __name__ == "__main__":
    main()
