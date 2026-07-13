import pandas as pd


INPUT_PATH = (
    "data/processed/cumulative_returns.csv"
)

OUTPUT_PATH = (
    "data/processed/drawdown.csv"
)


def calculate_drawdown(cumulative_returns):
    """
    Calculates the running drawdown of a portfolio.
    """

    drawdown = cumulative_returns.copy()

    drawdown["Running Peak"] = (
        drawdown["Wealth Index"]
        .cummax()
    )

    drawdown["Drawdown"] = (
        drawdown["Wealth Index"]
        /
        drawdown["Running Peak"]
        - 1
    )

    return drawdown


if __name__ == "__main__":

    cumulative = pd.read_csv(
        INPUT_PATH,
        parse_dates=["Date"]
    )

    drawdown = calculate_drawdown(
        cumulative
    )

    drawdown.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print(drawdown.head())

    print("\nWorst Drawdown:")

    print(
        drawdown["Drawdown"].min()
    )