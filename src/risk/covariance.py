import pandas as pd


RETURNS_PATH = (
    "data/processed/log_returns.csv"
)

COV_PATH = (
    "data/processed/covariance_matrix.csv"
)

CORR_PATH = (
    "data/processed/correlation_matrix.csv"
)


TRADING_DAYS = 252



def load_returns():

    return pd.read_csv(
        RETURNS_PATH,
        parse_dates=["Date"]
    )



def calculate_covariance(returns):

    assets = returns.columns[1:]


    daily_cov = (
        returns[assets]
        .cov()
    )


    annual_cov = (
        daily_cov *
        TRADING_DAYS
    )


    correlation = (
        returns[assets]
        .corr()
    )


    return annual_cov, correlation



if __name__ == "__main__":


    returns = load_returns()


    covariance, correlation = (
        calculate_covariance(
            returns
        )
    )


    covariance.to_csv(
        COV_PATH,
        index=True
    )


    correlation.to_csv(
        CORR_PATH,
        index=True
    )


    print("Files saved successfully")

    print(
        f"\nSaved covariance matrix to: {COV_PATH}"
    )

    print(
        f"Saved correlation matrix to: {CORR_PATH}"
    )


    print("\nCovariance shape:")
    print(covariance.shape)


    print("\nCorrelation shape:")
    print(correlation.shape)