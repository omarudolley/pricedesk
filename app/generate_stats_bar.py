from app.utils import analyze_memory
from app.utils import analyze_time
from app.utils import logger
from app.utils import save_as_json
from app.helper import generate_in_usd

import pandas as pd
import numpy as np
from app.constants import (
    LISTING_CSV_PATH,
    STATS_BAR_LRD_PATH,
    STATS_BAR_USD_PATH,
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

    mean_df_lrd = data_from_google_drive.groupby("Date").mean()
    mean_df_usd = generate_in_usd(mean_df_lrd)

    mean_df_lrd = mean_df_lrd.round(0)
    mean_df_usd = mean_df_usd.round(2)

    final_usd_data = {"updatedOn": TODAY_DMYHM}
    final_ld_data = {"updatedOn": TODAY_DMYHM}

    print(mean_df_lrd)

    for item in COMMODITY_LIST:
        final_ld_data[f"{item}_change"] = round(np.diff(mean_df_lrd[item])[-1], 2)
        final_usd_data[f"{item}_change"] = round(np.diff(mean_df_usd[item])[-1], 2)

    final_usd_data.update(mean_df_usd.iloc[-1])
    final_ld_data.update(mean_df_lrd.iloc[-1])

    save_as_json(STATS_BAR_USD_PATH, final_usd_data)
    save_as_json(STATS_BAR_LRD_PATH, final_ld_data)


if __name__ == "__main__":
    main()
