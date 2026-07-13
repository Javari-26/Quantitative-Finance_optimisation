import pandas as pd
from sklearn.covariance import LedoitWolf


RETURNS_PATH = (
    "data/processed/log_returns.csv"
)

OUTPUT_PATH = (
    "data/processed/shrunk_covariance_matrix.csv"
)


TRADING_DAYS = 252



def load_returns():

    return pd.read_csv(
        RETURNS_PATH,
        parse_dates=["Date"]
    )



def calculate_shrinkage_covariance(
        returns
):

    assets = returns.columns[1:]


    model = LedoitWolf()


    model.fit(
        returns[assets]
    )


    covariance = (
        model.covariance_
    )


    covariance = (
        covariance *
        TRADING_DAYS
    )


    covariance = pd.DataFrame(
        covariance,
        index=assets,
        columns=assets
    )


    return covariance



if __name__ == "__main__":


    returns = load_returns()


    covariance = (
        calculate_shrinkage_covariance(
            returns
        )
    )


    covariance.to_csv(
        OUTPUT_PATH
    )


    print(
        "Ledoit-Wolf Shrinkage Covariance"
    )

    print(covariance)