import numpy as np
import pandas as pd


TRADING_DAYS = 252


def annual_return(portfolio_returns):
    """
    Annualized return from daily log returns.
    """

    return portfolio_returns.mean() * TRADING_DAYS


def annual_volatility(portfolio_returns):
    """
    Annualized volatility.
    """

    return portfolio_returns.std() * np.sqrt(TRADING_DAYS)


def sharpe_ratio(
        portfolio_returns,
        risk_free_rate=0.0
):
    """
    Annualized Sharpe Ratio.
    """

    ret = annual_return(
        portfolio_returns
    )

    vol = annual_volatility(
        portfolio_returns
    )

    return (
        ret - risk_free_rate
    ) / vol


def downside_volatility(
        portfolio_returns
):
    """
    Downside deviation.
    """

    downside = portfolio_returns[
        portfolio_returns < 0
    ]

    return (
        downside.std()
        * np.sqrt(TRADING_DAYS)
    )


def sortino_ratio(
        portfolio_returns,
        risk_free_rate=0.0
):
    """
    Annualized Sortino Ratio.
    """

    ret = annual_return(
        portfolio_returns
    )

    downside = downside_volatility(
        portfolio_returns
    )

    return (
        ret - risk_free_rate
    ) / downside


def max_drawdown(
        cumulative_returns
):
    """
    Maximum drawdown.
    """

    running_max = (
        cumulative_returns.cummax()
    )

    drawdown = (
        cumulative_returns
        /
        running_max
    ) - 1

    return drawdown.min()


def calmar_ratio(
        portfolio_returns,
        cumulative_returns
):
    """
    Calmar Ratio.
    """

    ret = annual_return(
        portfolio_returns)

    mdd = abs(
        max_drawdown(
            cumulative_returns
        )
    )

    return ret / mdd


def value_at_risk(
        portfolio_returns,
        confidence=0.95
):
    """
    Historical VaR.
    """

    return np.percentile(
        portfolio_returns,
        (1 - confidence) * 100
    )


def conditional_value_at_risk(
        portfolio_returns,
        confidence=0.95
):
    """
    Historical CVaR.
    """

    var = value_at_risk(
        portfolio_returns,
        confidence
    )
  
    return portfolio_returns[
        portfolio_returns <= var
    ].mean()