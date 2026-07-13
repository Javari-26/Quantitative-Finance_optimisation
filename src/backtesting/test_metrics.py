import pandas as pd

from portfolio_returns import (
    calculate_portfolio_returns,
    load_returns
)

from performance_metrics import *


WEIGHTS = pd.read_csv(
    "data/processed/maximum_sharpe_weights.csv",
    index_col=0
).iloc[:, 0]


returns = load_returns()

portfolio = calculate_portfolio_returns(
    returns,
    WEIGHTS
)


daily = portfolio[
    "Portfolio Return"
]


cumulative = (
    1 + daily
).cumprod()


print("Annual Return")
print(
    annual_return(daily)
)

print("\nAnnual Volatility")
print(
    annual_volatility(daily)
)

print("\nSharpe Ratio")
print(
    sharpe_ratio(daily)
)

print("\nSortino Ratio")
print(
    sortino_ratio(daily)
)

print("\nMaximum Drawdown")
print(
    max_drawdown(cumulative)
)

print("\nCalmar Ratio")
print(
    calmar_ratio(
        daily,
        cumulative
    )
)

print("\nValue at Risk")
print(
    value_at_risk(daily)
)

print("\nConditional Value at Risk")
print(
    conditional_value_at_risk(daily)
)