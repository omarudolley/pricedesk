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

    data_from_google_drive.drop("Timestamp", inplace=True, axis=1)
    data_from_google_drive.drop("Location", inplace=True, axis=1)

    mean_df = data_from_google_drive.groupby("Date").mean()

    mean_df["Sum"] = mean_df.sum(axis=1)

    mean_df["pdt_chg"] = mean_df["Sum"].pct_change()

    data = mean_df["pdt_chg"].round(3).tolist()

    dates = list(set(data_from_google_drive["Date"]))
    dates.sort()
    final_ld_data = {"dates": dates, "data": data}

    save_as_json(INFLATION_DATA_PATH, final_ld_data)


if __name__ == "__main__":
    main()
