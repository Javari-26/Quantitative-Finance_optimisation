import numpy as np

from objective_functions import (
    portfolio_return,
    portfolio_volatility,
    portfolio_sharpe_ratio
)


weights = np.array(
    [
        0.25,
        0.25,
        0.25,
        0.25
    ]
)


returns = np.array(
    [
        0.10,
        0.12,
        0.08,
        0.15
    ]
)


covariance = np.array(
    [
        [0.04,0,0,0],
        [0,0.09,0,0],
        [0,0,0.16,0],
        [0,0,0,0.25]
    ]
)


print(
    "Return:",
    portfolio_return(
        weights,
        returns
    )
)


print(
    "Volatility:",
    portfolio_volatility(
        weights,
        covariance
    )
)


print(
    "Sharpe:",
    portfolio_sharpe_ratio(
        weights,
        returns,
        covariance
    )
)