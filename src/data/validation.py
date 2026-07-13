import pandas as pd


PRICES_PATH = "data/processed/prices.csv"


def load_prices():

    df = pd.read_csv(
        PRICES_PATH,
        parse_dates=["Date"]
    )

    return df



def check_missing_values(df):

    print("\n--- Missing Values ---")

    missing = df.isna().sum()

    print(missing[missing > 0])



def check_duplicates(df):

    print("\n--- Duplicate Dates ---")

    duplicates = df["Date"].duplicated().sum()

    print(
        f"Duplicate dates: {duplicates}"
    )



def check_date_order(df):

    print("\n--- Date Order ---")

    ordered = df["Date"].is_monotonic_increasing

    print(
        f"Dates ordered correctly: {ordered}"
    )



def check_dimensions(df):

    print("\n--- Dataset Size ---")

    print(
        f"Observations: {len(df)}"
    )

    print(
        f"Assets: {len(df.columns)-1}"
    )



def check_zero_prices(df):

    print("\n--- Zero Prices ---")

    zeros = (
        df.iloc[:,1:] == 0
    ).sum()

    print(
        zeros[zeros > 0]
    )



if __name__ == "__main__":

    prices = load_prices()

    check_dimensions(prices)

    check_missing_values(prices)

    check_duplicates(prices)

    check_date_order(prices)

    check_zero_prices(prices)