import pandas as pd


MIN_HISTORY = 0.90


def filter_assets(prices):

    total_days = len(prices)

    valid_assets = []


    for asset in prices.columns[1:]:

        availability = (
            prices[asset]
            .count()
            /
            total_days
        )


        print(
            asset,
            round(availability*100,2),
            "%"
        )


        if availability >= MIN_HISTORY:

            valid_assets.append(asset)



    return valid_assets



if __name__ == "__main__":


    prices = pd.read_csv(
        "data/processed/prices.csv"
    )


    assets = filter_assets(prices)


    print("\nFinal Universe:")
    print(assets)

    print(
        "\nNumber of Assets:",
        len(assets)
    )