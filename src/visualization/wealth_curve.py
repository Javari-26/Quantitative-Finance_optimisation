import pandas as pd
import matplotlib.pyplot as plt


INPUT_PATH = (
    "data/processed/cumulative_returns.csv"
)

OUTPUT_PATH = (
    "figures/wealth_curve.png"
)


def plot_wealth_curve():

    data = pd.read_csv(
        INPUT_PATH,
        parse_dates=["Date"]
    )

    plt.figure(
        figsize=(10,6)
    )

    plt.plot(
        data["Date"],
        data["Wealth Index"]
    )

    plt.title(
        "Growth of R1 Invested in Maximum Sharpe Portfolio"
    )

    plt.xlabel(
        "Date"
    )

    plt.ylabel(
        "Wealth Index"
    )

    plt.grid(
        True
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_PATH,
        dpi=300
    )

    plt.show()


if __name__ == "__main__":

    plot_wealth_curve()