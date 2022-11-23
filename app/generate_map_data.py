from app.utils import analyze_memory
from app.utils import analyze_time
from app.utils import logger
from app.utils import save_as_json
from app.helper import generate_in_usd, average_values_for_montserrado

import pandas as pd
import numpy as np
from app.constants import (
    LISTING_CSV_PATH,
    MAP_DATA_USD_PATH,
    MAP_DATA_LRD_PATH,
    COMMODITY_LIST,
    LOCATION,
    TODAY_DMYHM,
)


@analyze_time
@analyze_memory
def main():
    logger.info("Loading local data files")
    data_from_google_drive = pd.read_csv(LISTING_CSV_PATH)

    data_from_google_drive.drop("Timestamp", inplace=True, axis=1)
    dates = list(set(data_from_google_drive["Date"]))
    dates.sort()

    df = average_values_for_montserrado(data_from_google_drive, dates)

    df_usd = generate_in_usd(df)

    df = df.round(0)
    df_usd = df_usd.round(2)

    df.set_index(["Date", "Location"], inplace=True)
    df_usd.set_index(["Date", "Location"], inplace=True)

    final_usd_data = {"dates": dates, "updatedOn": TODAY_DMYHM}
    final_ld_data = {"dates": dates, "updatedOn": TODAY_DMYHM}

    for item in COMMODITY_LIST:
        _item = df.to_dict()[item]
        _item_usd = df_usd.to_dict()[item]

        final_ld_data.update(
            {
                item: [
                    {"date": d, "data": [[_item.get((d, l))] for l in LOCATION]}
                    for d in dates
                ]
            }
        )

        final_usd_data.update(
            {
                item: [
                    {"date": d, "data": [[_item_usd.get((d, l))] for l in LOCATION]}
                    for d in dates
                ]
            }
        )

    save_as_json(MAP_DATA_USD_PATH, final_usd_data)
    save_as_json(MAP_DATA_LRD_PATH, final_ld_data)


if __name__ == "__main__":
    main()
