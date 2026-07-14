import pandas as pd
import matplotlib.pyplot as plt
import os


# ----------------------------
# Paths
# ----------------------------

DATA_PATH = "data/processed"

REPORT_PATH = "reports"

FIGURE_PATH = "reports/figures"

TABLE_PATH = "reports/tables"


os.makedirs(FIGURE_PATH, exist_ok=True)
os.makedirs(TABLE_PATH, exist_ok=True)
os.makedirs(REPORT_PATH, exist_ok=True)



# ----------------------------
# Load data
# ----------------------------

def load_data():

    cumulative = pd.read_csv(
        f"{DATA_PATH}/cumulative_returns.csv",
        parse_dates=["Date"]
    )


    metrics = pd.read_csv(
        f"{DATA_PATH}/performance_metrics.csv"
    )


    return cumulative, metrics



# ----------------------------
# Equity Curve
# ----------------------------

def plot_equity_curve(data):

    plt.figure(figsize=(10,5))

    plt.plot(
        data["Date"],
        data["Wealth Index"]
    )

    plt.title(
        "Portfolio Growth Over Time"
    )

    plt.xlabel(
        "Date"
    )

    plt.ylabel(
        "Wealth Index"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        f"{FIGURE_PATH}/cumulative_returns.png",
        dpi=300
    )

    plt.close()



# ----------------------------
# Drawdown
# ----------------------------

def plot_drawdown(data):

    wealth = data["Wealth Index"]

    running_max = wealth.cummax()

    drawdown = (
        wealth - running_max
    ) / running_max


    plt.figure(figsize=(10,5))

    plt.plot(
        data["Date"],
        drawdown
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

    plt.grid(True)

    plt.tight_layout()


    plt.savefig(
        f"{FIGURE_PATH}/drawdown.png",
        dpi=300
    )

    plt.close()



# ----------------------------
# Portfolio Allocation
# ----------------------------

def plot_portfolio_allocation():

    weights = pd.read_csv(
        f"{DATA_PATH}/maximum_sharpe_weights.csv"
    )


    plt.figure(figsize=(10,5))


    plt.bar(
        weights.iloc[:,0],
        weights.iloc[:,1]
    )


    plt.title(
        "Maximum Sharpe Portfolio Allocation"
    )


    plt.xlabel(
        "Assets"
    )


    plt.ylabel(
        "Weight"
    )


    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()


    plt.savefig(
        f"{FIGURE_PATH}/portfolio_allocation.png",
        dpi=300
    )


    plt.close()



# ----------------------------
# Efficient Frontier
# ----------------------------

def plot_efficient_frontier():

    frontier = pd.read_csv(
        f"{DATA_PATH}/efficient_frontier.csv"
    )


    plt.figure(figsize=(10,5))


    plt.scatter(
        frontier.iloc[:,1],
        frontier.iloc[:,0],
        s=10
    )


    plt.title(
        "Efficient Frontier"
    )


    plt.xlabel(
        "Risk (Volatility)"
    )


    plt.ylabel(
        "Expected Return"
    )


    plt.grid(True)


    plt.tight_layout()


    plt.savefig(
        f"{FIGURE_PATH}/efficient_frontier.png",
        dpi=300
    )


    plt.close()



# ----------------------------
# Create Performance Table
# ----------------------------

def create_performance_table(metrics):

    table = metrics.copy()


    percentage_metrics = [
        "Annual Return",
        "Annual Volatility",
        "VaR 95%",
        "CVaR 95%",
        "Maximum Drawdown"
    ]


    table["Value"] = table.apply(
        lambda row:
        f"{row['Value']:.2%}"
        if row["Metric"] in percentage_metrics
        else f"{row['Value']:.3f}",
        axis=1
    )


    table.to_csv(
        f"{TABLE_PATH}/performance_table.csv",
        index=False
    )


    print(
        "Performance table created."
    )



# ----------------------------
# Text Summary
# ----------------------------

def create_summary(metrics):

    file = (
        f"{REPORT_PATH}/"
        "portfolio_summary.txt"
    )


    with open(file,"w") as f:


        f.write(
            "Portfolio Performance Report\n"
        )

        f.write(
            "===========================\n\n"
        )


        for _, row in metrics.iterrows():

            f.write(
                f"{row['Metric']}: "
                f"{row['Value']:.6f}\n"
            )



# ----------------------------
# Main
# ----------------------------

def main():

    cumulative, metrics = load_data()


    print(
        "Generating report..."
    )


    plot_equity_curve(
        cumulative
    )


    plot_drawdown(
        cumulative
    )


    plot_portfolio_allocation()


    plot_efficient_frontier()


    create_performance_table(
        metrics
    )


    create_summary(
        metrics
    )


    print(
        "Report components generated successfully."
    )



if __name__ == "__main__":
    main()