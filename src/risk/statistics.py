import pandas as pd
import numpy as np


RETURNS_PATH = (
    "data/processed/log_returns.csv"
)


OUTPUT_PATH = (
    "data/processed/asset_statistics.csv"
)

EXPECTED_RETURNS_PATH = (
    "data/processed/expected_returns.csv"
)


TRADING_DAYS = 252



def load_returns():

    return pd.read_csv(
        "data/processed/log_returns.csv",
        parse_dates=["Date"]
    )



def calculate_statistics(returns):

    assets = returns.columns[1:]


    stats = pd.DataFrame(
        index=assets
    )


    daily_mean = (
        returns[assets]
        .mean()
    )


    daily_vol = (
        returns[assets]
        .std()
    )


    stats["Annual Return"] = (
        daily_mean *
        TRADING_DAYS
    )


    stats["Annual Volatility"] = (
        daily_vol *
        np.sqrt(TRADING_DAYS)
    )


    stats["Sharpe Ratio"] = (
        stats["Annual Return"]
        /
        stats["Annual Volatility"]
    )


    return stats



if __name__ == "__main__":


    returns = load_returns()


    stats = calculate_statistics(
        returns
    )

    # Save full statistics
stats.to_csv(
    "data/processed/asset_statistics.csv"
)

# Save expected returns only
stats[["Annual Return"]].to_csv(
    "data/processed/expected_returns.csv"
)

print("Statistics saved.\n")
print(stats)

print("\nExpected returns saved.")


    


print(stats)
