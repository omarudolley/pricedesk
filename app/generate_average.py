from app.utils import analyze_memory
from app.utils import analyze_time
from app.utils import logger
from app.utils import read_json_from_file
from app.utils import save_as_json
from app.helper import generate_in_usd

import pandas as pd
from app.constants import (
    RED_LIGHT_LISTING_CSV_PATH,
    DUALA_LISTING_CSV_PATH,
    WATERSIDE_LISTING_CSV_PATH,
    AVERAGE_USD_PATH,
    AVERAGE_LRD_PATH,
)


@analyze_time
@analyze_memory
def main():

    logger.info("Loading local data files")
    data_from_duala = pd.read_csv(DUALA_LISTING_CSV_PATH)
    data_from_redlight = pd.read_csv(RED_LIGHT_LISTING_CSV_PATH)
    data_from_waterside = pd.read_csv(WATERSIDE_LISTING_CSV_PATH)

    combined_data = pd.concat(
        [
            pd.DataFrame(data_from_duala),
            pd.DataFrame(data_from_redlight),
            pd.DataFrame(data_from_waterside),
        ]
    )
    combined_data.drop("Timestamp", inplace=True, axis=1)

    average_date_lrd = combined_data.groupby("Date").mean()
    average_date_usd = generate_in_usd(average_date_lrd)

    average_date_lrd_dict = average_date_lrd.to_dict("index")
    average_date_usd_dict = average_date_usd.to_dict("index")

    save_as_json(AVERAGE_USD_PATH, average_date_usd_dict)
    save_as_json(AVERAGE_LRD_PATH, average_date_lrd_dict)


if __name__ == "__main__":
    main()
