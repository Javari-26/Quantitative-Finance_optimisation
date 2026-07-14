import pandas as pd
import numpy as np
import os


TRADING_DAYS = 252


# ----------------------------
# Paths
# ----------------------------

PRICE_FILE = (
    "data/processed/"
    "prices_clean.csv"
)


PORTFOLIO_FILE = (
    "data/processed/"
    "cumulative_returns.csv"
)


OUTPUT_FILE = (
    "data/processed/"
    "benchmark_metrics.csv"
)


COMPARISON_FILE = (
    "reports/tables/"
    "portfolio_vs_benchmark.csv"
)



# ----------------------------
# Metrics
# ----------------------------

def annual_return(returns):

    return returns.mean() * TRADING_DAYS



def annual_volatility(returns):

    return returns.std() * np.sqrt(TRADING_DAYS)



def sharpe_ratio(returns):

    return (
        returns.mean()
        /
        returns.std()
    ) * np.sqrt(TRADING_DAYS)



def sortino_ratio(returns):

    downside = returns[returns < 0]

    return (
        returns.mean()
        /
        downside.std()
    ) * np.sqrt(TRADING_DAYS)



def maximum_drawdown(returns):

    wealth = (
        1 + returns
    ).cumprod()


    peak = wealth.cummax()


    drawdown = (
        wealth - peak
    ) / peak


    return drawdown.min()



def calmar_ratio(returns):

    ann_return = annual_return(
        returns
    )

    max_dd = abs(
        maximum_drawdown(
            returns
        )
    )

    return ann_return / max_dd



# ----------------------------
# Create benchmark
# ----------------------------

def create_equal_weight_returns():

    prices = pd.read_csv(
        PRICE_FILE,
        parse_dates=["Date"]
    )


    prices = prices.set_index(
        "Date"
    )


    returns = prices.pct_change()

    returns = returns.dropna()


    # 17 stocks equal weights

    weights = np.ones(
        len(returns.columns)
    ) / len(returns.columns)


    benchmark_returns = (
        returns @ weights
    )


    return benchmark_returns



# ----------------------------
# Compare portfolios
# ----------------------------

def main():


    print(
        "Creating benchmark..."
    )


    benchmark_returns = (
        create_equal_weight_returns()
    )


    optimized = pd.read_csv(
        PORTFOLIO_FILE,
        parse_dates=["Date"]
    )


    optimized_returns = optimized[
        "Portfolio Return"
    ]



    results = pd.DataFrame({

        "Metric":[

            "Annual Return",
            "Annual Volatility",
            "Sharpe Ratio",
            "Sortino Ratio",
            "Maximum Drawdown",
            "Calmar Ratio"

        ],


        "Optimized Portfolio":[

            annual_return(
                optimized_returns
            ),

            annual_volatility(
                optimized_returns
            ),

            sharpe_ratio(
                optimized_returns
            ),

            sortino_ratio(
                optimized_returns
            ),

            maximum_drawdown(
                optimized_returns
            ),

            calmar_ratio(
                optimized_returns
            )

        ],


        "Equal Weight Benchmark":[

            annual_return(
                benchmark_returns
            ),

            annual_volatility(
                benchmark_returns
            ),

            sharpe_ratio(
                benchmark_returns
            ),

            sortino_ratio(
                benchmark_returns
            ),

            maximum_drawdown(
                benchmark_returns
            ),

            calmar_ratio(
                benchmark_returns
            )

        ]

    })


    os.makedirs(
        "reports/tables",
        exist_ok=True
    )


    results.to_csv(
        COMPARISON_FILE,
        index=False
    )


    print(results)


    print(
        "\nSaved:"
    )

    print(
        COMPARISON_FILE
    )



if __name__ == "__main__":

    main()