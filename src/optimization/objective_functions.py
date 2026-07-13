import numpy as np



def portfolio_return(
        weights,
        expected_returns
):
    """
    Calculate expected portfolio return

    Rp = w.T * μ
    """

    return np.dot(
        weights,
        expected_returns
    )



def portfolio_variance(
        weights,
        covariance_matrix
):
    """
    Calculate portfolio variance

    σ²p = w.T Σ w
    """

    return np.dot(
        weights.T,
        np.dot(
            covariance_matrix,
            weights
        )
    )



def portfolio_volatility(
        weights,
        covariance_matrix
):
    """
    Calculate portfolio volatility

    σp = sqrt(w.T Σ w)
    """

    variance = portfolio_variance(
        weights,
        covariance_matrix
    )


    return np.sqrt(
        variance
    )



def portfolio_sharpe_ratio(
        weights,
        expected_returns,
        covariance_matrix,
        risk_free_rate=0.0
):
    """
    Calculate Sharpe ratio

    S = (Rp - Rf) / σp
    """


    returns = portfolio_return(
        weights,
        expected_returns
    )


    volatility = portfolio_volatility(
        weights,
        covariance_matrix
    )


    return (
        (returns - risk_free_rate)
        /
        volatility
    )



def negative_sharpe_ratio(
        weights,
        expected_returns,
        covariance_matrix,
        risk_free_rate=0.0
):
    """
    Negative Sharpe for minimization algorithms
    """

    return -portfolio_sharpe_ratio(
        weights,
        expected_returns,
        covariance_matrix,
        risk_free_rate
    )