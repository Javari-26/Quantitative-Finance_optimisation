import numpy as np



def portfolio_constraint():

    return {
        "type": "eq",
        "fun": lambda weights:
            np.sum(weights) - 1
    }



def long_only_bounds(
        n_assets
):

    return [
        (0,1)
        for _ in range(n_assets)
    ]



def max_weight_bounds(
        n_assets,
        maximum=0.20
):

    return [
        (0, maximum)
        for _ in range(n_assets)
    ]