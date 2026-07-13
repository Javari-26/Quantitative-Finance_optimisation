import pandas as pd
import glob
import os


RAW_PATH = "data/raw/*.csv"
OUTPUT_PATH = "data/processed/prices.csv"


def load_stock_prices(file):

    # Get ticker name from filename
    ticker = os.path.basename(file).replace(".csv", "")

    # Read yfinance file
    df = pd.read_csv(
        file,
        skiprows=[1, 2]
    )


    # Keep only Date and Close
    df = df[
        ["Price", "Close"]
    ]


    # Rename columns
    df.columns = [
        "Date",
        ticker
    ]


    # Convert date
    df["Date"] = pd.to_datetime(
        df["Date"]
    )


    return df



def combine_prices():

    files = glob.glob(RAW_PATH)

    print(f"Loading {len(files)} files...")


    price_frames = []


    for file in files:

        print(
            "Processing:",
            os.path.basename(file)
        )

        df = load_stock_prices(file)

        price_frames.append(df)



    prices = price_frames[0]


    for df in price_frames[1:]:

        prices = prices.merge(
            df,
            on="Date",
            how="outer"
        )


    prices.sort_values(
        "Date",
        inplace=True
    )


    return prices



if __name__ == "__main__":


    prices = combine_prices()


    os.makedirs(
        "data/processed",
        exist_ok=True
    )


    prices.to_csv(
        OUTPUT_PATH,
        index=False
    )


    print("\nFinished!")
    print(prices.head())
    print(prices.shape)