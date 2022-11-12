from app.constants import GOOGLE_DRIVE_PATH_PREFIX, GOOGLE_DRIVE_PATH_SUFFIX


def generate_google_drive_url(doc_id: str):
    return GOOGLE_DRIVE_PATH_PREFIX + doc_id + GOOGLE_DRIVE_PATH_SUFFIX


def generate_in_usd(df):

    df_without_exchange_rates = df.loc[
        :, ~df.columns.isin(["USD buying rate", "USD selling rate", "Date"])
    ]

    exchange_rate = df["USD buying rate"]

    df_without_exchange_rates = df_without_exchange_rates.div(
        exchange_rate, axis="index"
    )

    combined_df = df_without_exchange_rates.combine_first(df)

    return combined_df

