import pandas as pd
import matplotlib.pyplot as plt


MIN_VAR_PATH = (
    "data/processed/minimum_variance_weights.csv"
)

MAX_SHARPE_PATH = (
    "data/processed/maximum_sharpe_weights.csv"
)


MIN_VAR_OUTPUT = (
    "figures/minimum_variance_weights.png"
)

MAX_SHARPE_OUTPUT = (
    "figures/maximum_sharpe_weights.png"
)



def plot_weights(path, output, title):

    weights = pd.read_csv(
        path,
        index_col=0
    )


    plt.figure(
        figsize=(10, 6)
    )


    plt.bar(
        weights.index,
        weights["Weight"]
    )


    plt.xlabel(
        "Assets"
    )


    plt.ylabel(
        "Portfolio Weight"
    )


    plt.title(
        title
    )


    plt.xticks(
        rotation=45
    )


    plt.grid(
        axis="y"
    )


    plt.tight_layout()


    plt.savefig(
        output,
        dpi=300
    )


    plt.show()



if __name__ == "__main__":

    plot_weights(
        MIN_VAR_PATH,
        MIN_VAR_OUTPUT,
        "Minimum Variance Portfolio Weights"
    )


    plot_weights(
        MAX_SHARPE_PATH,
        MAX_SHARPE_OUTPUT,
        "Maximum Sharpe Portfolio Weights"
    ) 
    