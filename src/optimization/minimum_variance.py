import pandas as pd
import numpy as np

from scipy.optimize import minimize

from objective_functions import (
    portfolio_variance
)

from constraints import (
    portfolio_constraint,
    max_weight_bounds
)


COV_PATH = (
    "data/processed/shrunk_covariance_matrix.csv"
)

OUTPUT_PATH = (
    "data/processed/minimum_variance_weights.csv"
)



def load_covariance():

    return pd.read_csv(
        COV_PATH,
        index_col=0
    )



def optimize_minimum_variance(
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

        portfolio_variance,

        initial_weights,

        args=(
            covariance.values,
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


    covariance = load_covariance()


    weights = optimize_minimum_variance(
        covariance
    )


    weights.to_csv(
        OUTPUT_PATH
    )


    print(
        "Minimum Variance Portfolio"
    )

    print(weights)


    print(
        "\nSum of weights:"
    )

    print(
        weights.sum()
    )