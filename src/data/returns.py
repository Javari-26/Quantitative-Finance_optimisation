import pandas as pd
import numpy as np


PRICE_PATH = "data/processed/prices_adjusted.csv" #changed after adjusting

SIMPLE_RETURN_PATH = (
    "data/processed/simple_returns.csv"
)

LOG_RETURN_PATH = (
    "data/processed/log_returns.csv"
)



def load_prices():

    return pd.read_csv(
        PRICE_PATH,
        parse_dates=["Date"]
    )



def calculate_returns(prices):

    returns = prices.copy()

    assets = prices.columns[1:]


    # Simple returns

    simple_returns = (
        prices[assets]
        .pct_change()
    )


    simple_returns.insert(
        0,
        "Date",
        prices["Date"]
    )


    simple_returns.dropna(
        inplace=True
    )


    # Log returns

    log_returns = np.log(
        prices[assets] /
        prices[assets].shift(1)
    )


    log_returns.insert(
        0,
        "Date",
        prices["Date"]
    )


    log_returns.dropna(
        inplace=True
    )


    return simple_returns, log_returns



if __name__ == "__main__":


    prices = load_prices()


    simple, log = calculate_returns(
        prices
    )


    simple.to_csv(
        SIMPLE_RETURN_PATH,
        index=False
    )


    log.to_csv(
        LOG_RETURN_PATH,
        index=False
    )


    print("Returns created")

    print("\nSimple returns:")
    print(simple.head())


    print("\nLog returns:")
    print(log.head())


    print("\nShape:")
    print(simple.shape)