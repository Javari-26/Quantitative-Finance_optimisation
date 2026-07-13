import pandas as pd
import numpy as np

from scipy.optimize import minimize

from objective_functions import (
    portfolio_return,
    portfolio_volatility
)

from constraints import (
    portfolio_constraint,
    max_weight_bounds
)


RETURNS_PATH = "data/processed/expected_returns.csv"

COVARIANCE_PATH = (
    "data/processed/shrunk_covariance_matrix.csv"
)

OUTPUT_PATH = (
    "data/processed/efficient_frontier.csv"
)


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


def optimize_target_return(
        target_return,
        expected_returns,
        covariance
):

    n_assets = len(expected_returns)

    initial_weights = (
        np.ones(n_assets)
        /
        n_assets
    )

    constraints = [

        portfolio_constraint(),

        {
            "type": "eq",

            "fun":
            lambda w:
            portfolio_return(
                w,
                expected_returns.values
            )
            -
            target_return
        }

    ]

    result = minimize(

        portfolio_volatility,

        initial_weights,

        args=(
            covariance.values,
        ),

        method="SLSQP",

        bounds=max_weight_bounds(
            n_assets,
            maximum=0.20
        ),

        constraints=constraints

    )

    return result


if __name__ == "__main__":

    expected_returns = load_expected_returns()

    covariance = load_covariance()

    frontier = []

    targets = np.linspace(

        expected_returns.min(),

        expected_returns.max(),

        100

    )

    for target in targets:

        result = optimize_target_return(

            target,

            expected_returns,

            covariance

        )

        if result.success:

            frontier.append({

                "Return":
                portfolio_return(
                    result.x,
                    expected_returns.values
                ),

                "Volatility":
                portfolio_volatility(
                    result.x,
                    covariance.values
                ),

                "Sharpe":
                portfolio_return(
                    result.x,
                    expected_returns.values
                )
                /
                portfolio_volatility(
                    result.x,
                    covariance.values
                )

            })

    frontier = pd.DataFrame(frontier)

    frontier.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print(frontier.head())