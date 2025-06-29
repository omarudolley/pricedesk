from app.utils import analyze_memory
from app.utils import analyze_time
from app.utils import logger
from app.utils import save_as_json
from app.helper import generate_in_usd

import pandas as pd
import numpy as np
from app.constants import (
    LISTING_CSV_PATH,
    INFLATION_DATA_PATH,
    COMMODITY_LIST,
    TODAY_DMYHM,
)


@analyze_time
@analyze_memory
def main():
    logger.info("Loading local data files")
    df = pd.read_csv(LISTING_CSV_PATH)

    # Drop optional columns if they exist
    df.drop(columns=["Timestamp", "Location"], errors="ignore", inplace=True)

    # Convert Date to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.dropna(subset=["Date"], inplace=True)

    # Add Month column for grouping
    df["Month"] = df["Date"].dt.to_period("M")

    # Select numeric columns only
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if "Date" in numeric_cols:
        numeric_cols.remove("Date")

    if not numeric_cols:
        logger.warning("No numeric columns found for inflation analysis.")
        return

    # Group by month and compute mean prices
    monthly_avg = df.groupby("Month")[numeric_cols].mean()

    # Ensure chronological order
    monthly_avg.sort_index(inplace=True)

    # Sum of all mean prices per month = simple price index
    monthly_avg["PriceIndex"] = monthly_avg.sum(axis=1)

    # Calculate month-over-month inflation rate
    monthly_avg["InflationRate"] = monthly_avg["PriceIndex"].pct_change() * 100

    final_ld_data = {
        "dates": monthly_avg.index.astype(str).tolist(),
        "data": monthly_avg["InflationRate"].round(2).where(pd.notnull).tolist()
    }
    
    save_as_json(INFLATION_DATA_PATH, final_ld_data)


if __name__ == "__main__":
    main()
