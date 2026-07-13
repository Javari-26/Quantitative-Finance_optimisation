import pandas as pd


PRICES_PATH = "data/processed/prices.csv"
OUTPUT_PATH = "data/processed/prices_clean.csv"


ASSETS = [
    "ABSA",
    "ANGLO",
    "BIDVEST",
    "CAPITEC",
    "DISCOVERY",
    "FIRSTRAND",
    "GOLDFIELDS",
    "MRPRICE",
    "MTN",
    "NASPERS",
    "NEDBANK",
    "SANLAM",
    "SASOL",
    "SHOPRITE",
    "STANDARDBANK",
    "VODACOM",
    "WOOLWORTHS"
]


def create_clean_prices():

    prices = pd.read_csv(
        PRICES_PATH,
        parse_dates=["Date"]
    )


    clean_prices = prices[
        ["Date"] + ASSETS
    ]


    clean_prices.to_csv(
        OUTPUT_PATH,
        index=False
    )


    return clean_prices



if __name__ == "__main__":

    df = create_clean_prices()


    print(df.head())

    print("\nShape:")
    print(df.shape)