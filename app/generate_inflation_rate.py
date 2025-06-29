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

   # Drop optional or irrelevant columns
    df.drop(columns=["Timestamp", "Location"], errors="ignore", inplace=True)

    # Parse the date column assuming MM/DD/YYYY format
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y", errors="coerce")

    # Remove rows with invalid or missing dates
    df.dropna(subset=["Date"], inplace=True)

    # Convert dates to monthly period for grouping
    df["Month"] = df["Date"].dt.to_period("M")

    # Select numeric columns (assumed to be prices)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if "Date" in numeric_cols:
        numeric_cols.remove("Date")

    if not numeric_cols:
        logger.warning("No numeric columns found for price analysis.")
        return

    # Group data by month and calculate the mean for each product/category
    monthly_avg = df.groupby("Month")[numeric_cols].mean()

    # Sort by month (important for percent change calculation)
    monthly_avg.sort_index(inplace=True)

    # Create a simple price index as the sum of monthly means
    monthly_avg["PriceIndex"] = monthly_avg.sum(axis=1)

    # Calculate month-to-month inflation as percent change
    monthly_avg["InflationRate"] = monthly_avg["PriceIndex"].pct_change() * 100

    # Prepare final dictionary for JSON output
    final_ld_data = {
        "dates": monthly_avg.index.astype(str).tolist(),
        "data": monthly_avg["InflationRate"].round(2).where(pd.notnull).tolist()
    }

    
    save_as_json(INFLATION_DATA_PATH, final_ld_data)


if __name__ == "__main__":
    main()
