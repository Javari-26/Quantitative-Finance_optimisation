import pandas as pd
import numpy as np


OUTPUT_PATH = (
    "data/processed/cumulative_returns.csv"
)


def calculate_cumulative_returns(
        portfolio_returns
):
    """
    Computes cumulative wealth index from daily log returns.

    Starting wealth = 1.
    """

    cumulative = (
        portfolio_returns.copy()
    )

    cumulative["Wealth Index"] = np.exp(
        cumulative["Portfolio Return"].cumsum()
        
    )

    return cumulative


if __name__ == "__main__":

    from portfolio_returns import (
        load_returns,
        calculate_portfolio_returns
    )

    weights = pd.read_csv(
        "data/processed/maximum_sharpe_weights.csv",
        index_col=0
    ).iloc[:, 0]

    returns = load_returns()

    portfolio = calculate_portfolio_returns(
        returns,
        weights
    )

    cumulative = calculate_cumulative_returns(
        portfolio
    )

    cumulative.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print(cumulative.head())

    print("\nLast observations:\n")

    print(cumulative.tail())