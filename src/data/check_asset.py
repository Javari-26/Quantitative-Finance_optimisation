import pandas as pd


df = pd.read_csv(
    "data/processed/prices.csv",
    parse_dates=["Date"]
)


richemont = df[
    ["Date","RICHEMONT"]
]


print(richemont.head(20))


print("\nLast available dates:")

print(
    richemont.dropna()
    .tail(20)
)


print("\nFirst available date:")

print(
    richemont.dropna()
    .iloc[0]
)