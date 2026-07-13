import pandas as pd
import numpy as np


RETURNS_PATH = (
    "data/processed/log_returns.csv"
)


def load_returns():

    return pd.read_csv(
        RETURNS_PATH,
        parse_dates=["Date"]
    )


def calculate_portfolio_returns(
        returns,
        weights
):
    """
    Calculates daily portfolio returns.
    """

    assets = weights.index

    portfolio = np.dot(
        returns[assets],
        weights.values
    )

    portfolio = pd.DataFrame({

        "Date": returns["Date"],

        "Portfolio Return": portfolio

    })

    return portfolio


if __name__ == "__main__":

    returns = load_returns()

    print(returns.head())