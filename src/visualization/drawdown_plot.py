import pandas as pd
import matplotlib.pyplot as plt


INPUT_PATH = (
    "data/processed/drawdown.csv"
)

OUTPUT_PATH = (
    "figures/drawdown_plot.png"
)



def plot_drawdown():

    data = pd.read_csv(
        INPUT_PATH,
        parse_dates=["Date"]
    )


    plt.figure(
        figsize=(10,6)
    )


    plt.plot(
        data["Date"],
        data["Drawdown"]
    )


    plt.title(
        "Portfolio Drawdown"
    )

    plt.xlabel(
        "Date"
    )

    plt.ylabel(
        "Drawdown"
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

    plot_drawdown()