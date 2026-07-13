import pandas as pd
import numpy as np

from scipy.optimize import minimize

from objective_functions import (
    negative_sharpe_ratio
)

from constraints import (
    portfolio_constraint,
    max_weight_bounds
)


RETURNS_PATH = (
    "data/processed/expected_returns.csv"
)

COVARIANCE_PATH = (
    "data/processed/shrunk_covariance_matrix.csv"
)

OUTPUT_PATH = (
    "data/processed/maximum_sharpe_weights.csv"
)

RISK_FREE_RATE = 0.0


def load_expected_returns():

    returns = pd.read_csv(
        RETURNS_PATH,
        index_col=0
    )

    return returns["Annual Return"]


def load_covariance():

    return pd.read_csv(
        COVARIANCE_PATH,
        index_col=0
    )


def optimize_maximum_sharpe(
        expected_returns,
        covariance
):

    assets = covariance.columns

    n_assets = len(assets)

    initial_weights = (
        np.ones(n_assets)
        /
        n_assets
    )

    result = minimize(

        negative_sharpe_ratio,

        initial_weights,

        args=(
            expected_returns.values,
            covariance.values,
            RISK_FREE_RATE
        ),

        method="SLSQP",

        bounds=max_weight_bounds(
            n_assets,
            maximum=0.20
        ),

        constraints=[
            portfolio_constraint()
        ]

    )

    if not result.success:

        raise Exception(
            result.message
        )

    weights = pd.Series(
        result.x,
        index=assets,
        name="Weight"
    )

    return weights


if __name__ == "__main__":

    expected_returns = load_expected_returns()

    covariance = load_covariance()

    weights = optimize_maximum_sharpe(
        expected_returns,
        covariance
    )

    weights.to_csv(
        OUTPUT_PATH
    )

    print(
        "Maximum Sharpe Portfolio"
    )

    print(weights)

    print(
        "\nSum of weights:"
    )

    print(
        weights.sum()
    )