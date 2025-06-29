from app.utils import analyze_memory
from app.utils import analyze_time
from app.utils import logger
from app.utils import save_as_json
from app.helper import generate_in_usd

import pandas as pd
import numpy as np
import pytz
from datetime import datetime
from app.constants import (
    LISTING_CSV_PATH,
    STATS_BAR_LRD_PATH,
    STATS_BAR_USD_PATH,
    COMMODITY_LIST,
    TODAY_DMYHM,
)

LOCAL_TZ = pytz.timezone("Africa/Monrovia")
TODAY_DMYHM = datetime.now(LOCAL_TZ).strftime("%d/%m/%Y %H:%M")

@analyze_time
@analyze_memory
def main():
    logger.info("Loading local data files")
    df = pd.read_csv(LISTING_CSV_PATH)

    # Clean and preprocess
    df.drop(columns=["Timestamp", "Location"], inplace=True, errors="ignore")

    # Parse dates properly and keep them as datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    df.dropna(subset=["Date"], inplace=True)

    # Group by date and average numeric columns
    mean_df_lrd = df.groupby("Date").mean().sort_index()  
    mean_df_usd = generate_in_usd(mean_df_lrd)

    # Round for output
    mean_df_lrd = mean_df_lrd.round(0)
    mean_df_usd = mean_df_usd.round(2)

    # Prepare final outputs
    final_usd_data = {"updatedOn": TODAY_DMYHM}
    final_ld_data = {"updatedOn": TODAY_DMYHM}

    for item in COMMODITY_LIST:
        try:
            # Calculate most recent change and last recorded value
            diff_lrd = round(mean_df_lrd[item].iloc[-1] - mean_df_lrd[item].iloc[-2], 2)
            diff_usd = round(mean_df_usd[item].iloc[-1] - mean_df_usd[item].iloc[-2], 2)

            final_ld_data[f"{item}_change"] = diff_lrd
            final_usd_data[f"{item}_change"] = diff_usd

            final_ld_data[f"{item}_last_recorded"] = float(mean_df_lrd[item].iloc[-2])
            final_usd_data[f"{item}_last_recorded"] = float(mean_df_usd[item].iloc[-2])
        except Exception as e:
            logger.warning(f"Skipping {item} due to error: {e}")

    # Append the most recent prices
    final_ld_data.update(mean_df_lrd.iloc[-1].to_dict())
    final_usd_data.update(mean_df_usd.iloc[-1].to_dict())


    save_as_json(STATS_BAR_USD_PATH, final_usd_data)
    save_as_json(STATS_BAR_LRD_PATH, final_ld_data)


if __name__ == "__main__":
    main()
