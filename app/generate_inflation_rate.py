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
    data_from_google_drive = pd.read_csv(LISTING_CSV_PATH)

    # Clean optional columns
    df.drop(columns=["Timestamp", "Location"], errors="ignore", inplace=True)

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.dropna(subset=["Date"], inplace=True)

    df["Month"] = df["Date"].dt.to_period("M")

    numeric_cols = df.select_dtypes(include="number").columns
    if "Date" in numeric_cols:
        numeric_cols = numeric_cols.drop("Date")

    monthly_avg = df.groupby("Month")[numeric_cols].mean()

    monthly_avg["PriceIndex"] = monthly_avg.sum(axis=1)

    monthly_avg["InflationRate"] = monthly_avg["PriceIndex"].pct_change() * 100

    final_ld_data = {
        "dates": monthly_avg.index.astype(str).tolist(),
        "data": monthly_avg["InflationRate"].round(2).fillna(None).tolist()
    }
    
    save_as_json(INFLATION_DATA_PATH, final_ld_data)


if __name__ == "__main__":
    main()
