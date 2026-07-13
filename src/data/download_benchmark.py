import yfinance as yf
import pandas as pd


OUTPUT_PATH = (
    "data/processed/alsi_prices.csv"
)


def download_alsi():

    ticker = "^J203.JO"

    data = yf.download(
        ticker,
        start="1995-06-30",
        end="2025-09-12"
    )


    prices = data["Close"]


    prices.to_csv(
        OUTPUT_PATH
    )


    print("ALSI benchmark downloaded successfully")
    print(prices.head())



if __name__ == "__main__":

    download_alsi()