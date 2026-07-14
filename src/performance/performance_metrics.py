import pandas as pd
import numpy as np
from scipy.stats import norm


TRADING_DAYS = 252


def annual_return(returns):
    """
    Annualized portfolio return
    """
    return returns.mean() * TRADING_DAYS



def annual_volatility(returns):
    """
    Annualized volatility
    """
    return returns.std() * np.sqrt(TRADING_DAYS)



def sharpe_ratio(returns, risk_free_rate=0):
    """
    Annualized Sharpe Ratio
    """

    excess_return = returns.mean() - risk_free_rate / TRADING_DAYS

    return (
        excess_return / returns.std()
    ) * np.sqrt(TRADING_DAYS)



def sortino_ratio(returns, risk_free_rate=0):
    """
    Downside risk adjusted return
    """

    downside = returns[returns < 0]

    downside_std = downside.std()

    return (
        (returns.mean() - risk_free_rate/TRADING_DAYS)
        /
        downside_std
    ) * np.sqrt(TRADING_DAYS)



def value_at_risk(returns, confidence=0.95):
    """
    Historical VaR
    """

    return np.percentile(
        returns,
        (1-confidence)*100
    )



def conditional_var(returns, confidence=0.95):
    """
    Historical CVaR
    """

    var = value_at_risk(
        returns,
        confidence
    )

    return returns[
        returns <= var
    ].mean()



def maximum_drawdown(wealth_index):
    """
    Maximum drawdown
    """

    running_max = wealth_index.cummax()

    drawdown = (
        wealth_index - running_max
    ) / running_max


    return drawdown.min()



def calmar_ratio(
    annual_ret,
    max_drawdown
):

    return annual_ret / abs(max_drawdown)



def main():

    # -----------------------------
    # Load cumulative returns
    # -----------------------------

    file_path = (
        "data/processed/"
        "cumulative_returns.csv"
    )


    data = pd.read_csv(
        file_path,
        parse_dates=["Date"]
    )


    returns = data[
        "Portfolio Return"
    ]


    wealth = data[
        "Wealth Index"
    ]


    # -----------------------------
    # Calculate metrics
    # -----------------------------

    ann_return = annual_return(
        returns
    )


    ann_vol = annual_volatility(
        returns
    )


    sharpe = sharpe_ratio(
        returns
    )


    sortino = sortino_ratio(
        returns
    )


    var95 = value_at_risk(
        returns,
        0.95
    )


    cvar95 = conditional_var(
        returns,
        0.95
    )


    max_dd = maximum_drawdown(
        wealth
    )


    calmar = calmar_ratio(
        ann_return,
        max_dd
    )


    # -----------------------------
    # Save results
    # -----------------------------


    metrics = pd.DataFrame({

        "Metric":[
            "Annual Return",
            "Annual Volatility",
            "Sharpe Ratio",
            "Sortino Ratio",
            "VaR 95%",
            "CVaR 95%",
            "Maximum Drawdown",
            "Calmar Ratio"
        ],


        "Value":[
            ann_return,
            ann_vol,
            sharpe,
            sortino,
            var95,
            cvar95,
            max_dd,
            calmar
        ]

    })


    output = (
        "data/processed/"
        "performance_metrics.csv"
    )


    metrics.to_csv(
        output,
        index=False
    )


    print("\nPerformance Metrics")
    print("-------------------")
    print(metrics)


    print(
        f"\nSaved to {output}"
    )



if __name__ == "__main__":
    main()