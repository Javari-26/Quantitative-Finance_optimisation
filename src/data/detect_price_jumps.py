import pandas as pd


PRICE_PATH = "data/processed/prices_clean.csv"


prices = pd.read_csv(
    PRICE_PATH,
    parse_dates=["Date"]
)


assets = prices.columns[1:]


for asset in assets:

    ratio = (
        prices[asset]
        /
        prices[asset].shift(1)
    )


    jumps = prices.loc[
        (ratio > 2) |
        (ratio < 0.5),
        ["Date", asset]
    ]


    if len(jumps) > 0:

        print("\n", asset)

        print(jumps)