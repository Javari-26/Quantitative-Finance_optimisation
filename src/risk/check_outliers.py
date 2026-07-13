import pandas as pd


RETURNS_PATH = (
    "data/processed/log_returns.csv"
)


returns = pd.read_csv(
    RETURNS_PATH,
    parse_dates=["Date"]
)


assets = returns.columns[1:]


for asset in assets:

    extreme = returns[
        abs(returns[asset]) > 0.20
    ]

    if len(extreme) > 0:

        print("\n", asset)

        print(
            extreme[
                ["Date", asset]
            ]
        )