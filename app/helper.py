from app.constants import GOOGLE_DRIVE_PATH_PREFIX, GOOGLE_DRIVE_PATH_SUFFIX
import pandas as pd


def generate_google_drive_url(doc_id: str):
    return GOOGLE_DRIVE_PATH_PREFIX + doc_id + GOOGLE_DRIVE_PATH_SUFFIX


def generate_in_usd(df):
    df_without_exchange_rates = df.loc[
        :, ~df.columns.isin(["USD buying rate", "USD selling rate", "Date", "Location"])
    ]

    exchange_rate = df["USD buying rate"]

    df_without_exchange_rates = df_without_exchange_rates.div(
        exchange_rate, axis="index"
    )

    combined_df = df_without_exchange_rates.combine_first(df)

    return combined_df


def average_values_for_montserrado(df, date):
    mont_region = df.loc[df["Location"].isin(["Duala", "Redlight", "Waterside"])]

    average_mont_region = mont_region.groupby(["Date"]).mean()
    average_mont_region = average_mont_region.assign(Location="Montserrado")

    average_mont_region.reset_index(drop=True, inplace=True)
    average_mont_region = average_mont_region.assign(Date=date)

    df = df[~df["Location"].isin(["Duala", "Redlight", "Waterside"])]

    combined_df = pd.concat([df, average_mont_region])

    return combined_df
