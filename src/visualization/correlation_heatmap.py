import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


INPUT_PATH = (
    "data/processed/simple_returns.csv"
)

OUTPUT_PATH = (
    "figures/correlation_heatmap.png"
)



def plot_correlation_heatmap():

    # Load simple returns
    returns = pd.read_csv(
        INPUT_PATH,
        parse_dates=["Date"],
        index_col="Date"
    )


    # Calculate correlations
    correlation_matrix = returns.corr()


    plt.figure(
        figsize=(12, 10)
    )


    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5
    )


    plt.title(
        "JSE Stock Return Correlation Matrix"
    )


    plt.tight_layout()


    plt.savefig(
        OUTPUT_PATH,
        dpi=300
    )


    plt.show()



if __name__ == "__main__":

    plot_correlation_heatmap()