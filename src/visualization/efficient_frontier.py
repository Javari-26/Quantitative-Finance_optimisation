import pandas as pd
import matplotlib.pyplot as plt


INPUT_PATH = (
    "data/processed/efficient_frontier.csv"
)

OUTPUT_PATH = (
    "figures/efficient_frontier.png"
)



def plot_efficient_frontier():

    data = pd.read_csv(
        INPUT_PATH
    )


    plt.figure(
        figsize=(10, 6)
    )


    scatter = plt.scatter(
        data["Volatility"],
        data["Return"],
        c=data["Sharpe"],
        cmap="viridis",
        s=15
    )


    plt.colorbar(
        scatter,
        label="Sharpe Ratio"
    )


    plt.xlabel(
        "Portfolio Volatility"
    )


    plt.ylabel(
        "Expected Return"
    )


    plt.title(
        "Efficient Frontier"
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

    plot_efficient_frontier()