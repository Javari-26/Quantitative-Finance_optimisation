import pandas as pd


INPUT = "data/processed/prices_clean.csv"
OUTPUT = "data/processed/prices_adjusted.csv"



def adjust_price_jumps(df):

    assets = df.columns[1:]


    for asset in assets:

        for i in range(1, len(df)):

            previous = df.loc[i-1, asset]
            current = df.loc[i, asset]


            ratio = current / previous


            if ratio > 50:

                print(
                    f"Adjusting {asset} on {df.loc[i,'Date']} downward"
                )

                df.loc[i:, asset] /= 100



            elif ratio < 0.02:

                print(
                    f"Adjusting {asset} on {df.loc[i,'Date']} upward"
                )

                df.loc[i:, asset] *= 100


    return df



if __name__ == "__main__":


    prices = pd.read_csv(
        INPUT,
        parse_dates=["Date"]
    )


    prices = adjust_price_jumps(prices)


    prices.to_csv(
        OUTPUT,
        index=False
    )


    print("Adjustment complete")