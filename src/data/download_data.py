import os
import yfinance as yf
import pandas as pd

from src.config import START_DATE, END_DATE


# JSE tickers (Yahoo Finance)
JSE_TICKERS = {
    "ABSA": "ABG.JO",
    "ANGLO": "AGL.JO",
    "BIDVEST": "BVT.JO",
    "CAPITEC": "CPI.JO",
    "DISCOVERY": "DSY.JO",
    "FIRSTRAND": "FSR.JO",
    "GOLDFIELDS": "GFI.JO",
    "MRPRICE": "MRP.JO",
    "MTN": "MTN.JO",
    "NASPERS": "NPN.JO",
    "NEDBANK": "NED.JO",
    "RICHEMONT": "CFR.JO",
    "SANLAM": "SLM.JO",
    "SASOL": "SOL.JO",
    "SHOPRITE": "SHP.JO",
    "STANDARDBANK": "SBK.JO",
    "VODACOM": "VOD.JO",
    "WOOLWORTHS": "WHL.JO"
}


RAW_DATA_PATH = "data/raw"


def create_directory():

    os.makedirs(RAW_DATA_PATH, exist_ok=True)


def download_stock(ticker, symbol):

    print(f"Downloading {ticker}...")

    df = yf.download(
        symbol,
        start=START_DATE,
        end=END_DATE,
        progress=False,
        auto_adjust=True
    )

    if df.empty:
        print(f"{ticker} download failed.")
        return

    filename = os.path.join(RAW_DATA_PATH, f"{ticker}.csv")

    df.to_csv(filename)

    print(f"Saved -> {filename}")


def download_all():

    create_directory()

    for ticker, symbol in JSE_TICKERS.items():
        download_stock(ticker, symbol)


if __name__ == "__main__":
    download_all()