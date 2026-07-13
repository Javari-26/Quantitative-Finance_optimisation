import pandas as pd
import matplotlib.pyplot as plt


PORTFOLIO_PATH = (
    "data/processed/cumulative_returns.csv"
)

ALSI_PATH = (
    "data/processed/alsi_prices.csv"
)

OUTPUT_PATH = (
    "figures/portfolio_vs_alsi.png"
)



def plot_benchmark_comparison():

    # -----------------------------
    # Load portfolio cumulative data
    # -----------------------------
    portfolio = pd.read_csv(
        PORTFOLIO_PATH,
        parse_dates=["Date"]
    )


    portfolio = portfolio.set_index(
        "Date"
    )


    # Convert portfolio returns into cumulative growth
    portfolio_cumulative = (
        1 + portfolio.iloc[:, 0]
    ).cumprod()



    # -----------------------------
    # Load ALSI benchmark prices
    # -----------------------------
    alsi = pd.read_csv(
        ALSI_PATH,
        parse_dates=["Date"]
    )


    alsi = alsi.set_index(
        "Date"
    )


    # Convert ALSI prices into cumulative growth
    alsi_returns = (
        alsi.iloc[:, 0]
        .pct_change()
        .dropna()
    )


    alsi_cumulative = (
        1 + alsi_returns
    ).cumprod()



    # -----------------------------
    # Align dates
    # -----------------------------
    comparison = pd.concat(
        [
            portfolio_cumulative,
            alsi_cumulative
        ],
        axis=1
    ).dropna()



    comparison.columns = [
        "Optimized Portfolio",
        "JSE ALSI"
    ]



    # -----------------------------
    # Normalize both to Growth of R1
    # -----------------------------
    comparison = (
        comparison /
        comparison.iloc[0]
    )



    # -----------------------------
    # Plot
    # -----------------------------
    plt.figure(
        figsize=(12, 6)
    )


    plt.plot(
        comparison.index,
        comparison["Optimized Portfolio"],
        label="Optimized Portfolio"
    )


    plt.plot(
        comparison.index,
        comparison["JSE ALSI"],
        label="JSE ALSI"
    )


    plt.xlabel(
        "Date"
    )


    plt.ylabel(
        "Growth of R1"
    )


    plt.title(
        "Optimized Portfolio vs JSE All Share Index"
    )


    plt.legend()


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

    plot_benchmark_comparison()



