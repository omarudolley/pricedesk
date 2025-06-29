from app.constants import GOOGLE_DRIVE_PATH_PREFIX, GOOGLE_DRIVE_PATH_SUFFIX
import pandas as pd


def generate_google_drive_url(doc_id: str):
    return GOOGLE_DRIVE_PATH_PREFIX + doc_id + GOOGLE_DRIVE_PATH_SUFFIX


def generate_in_usd(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts commodity prices in LRD to USD using the 'USD buying rate'.

    Assumes 'USD buying rate' is available per row and that prices are in LRD.
    """
    # Make a copy to avoid changing original
    df = df.copy()

    # Identify columns to convert (exclude exchange rate and non-numeric fields)
    exclude_cols = ["USD buying rate", "USD selling rate", "Date", "Location"]
    numeric_cols = df.columns.difference(exclude_cols)

    # Get exchange rate
    exchange_rate = df["USD buying rate"]

    # Divide each commodity column by exchange rate to convert to USD
    df_usd = df[numeric_cols].div(exchange_rate, axis=0)

    # Reattach metadata columns (Date, Location, etc.)
    for col in exclude_cols:
        if col in df:
            df_usd[col] = df[col]

    return df_usd



def average_values_for_montserrado(df: pd.DataFrame, dates: list[str]) -> pd.DataFrame:
    """
    Computes the average values for key markets in Montserrado and appends
    a new row with 'Location' set to 'Montserrado'.

    Arguments:
    - df: Original dataframe
    - dates: Sorted list of dates as strings to be assigned for final output

    Returns:
    - df: Original df plus averaged Montserrado rows
    """
    df = df.copy()

    # Filter Montserrado locations
    mont_df = df[df["Location"].isin(["Duala", "Redlight", "Waterside"])]

    # Group by Date and take mean
    mont_avg = mont_df.groupby("Date").mean(numeric_only=True).reset_index()

    # Set location to "Montserrado"
    mont_avg["Location"] = "Montserrado"

    # Replace date column with correct format if needed
    if isinstance(dates, list) and len(dates) == len(mont_avg):
        mont_avg["Date"] = dates
    else:
        # fallback: keep existing dates
        logger.warning("Date list length mismatch; using original dates.")

    # Remove original locations to avoid double-counting
    df = df[~df["Location"].isin(["Duala", "Redlight", "Waterside"])]

    # Combine with averaged Montserrado rows
    combined_df = pd.concat([df, mont_avg], ignore_index=True)

    return combined_df

