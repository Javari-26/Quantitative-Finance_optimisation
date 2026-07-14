from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

import pandas as pd
import os



# ----------------------------
# Paths
# ----------------------------

REPORT_PATH = "reports"

FIGURE_PATH = "reports/figures"

TABLE_PATH = "reports/tables"


OUTPUT_FILE = (
    f"{REPORT_PATH}/"
    "Portfolio_Optimization_Report.pdf"
)



# ----------------------------
# Helper function
# ----------------------------

def create_table(df):

    data = [
        list(df.columns)
    ]


    for row in df.values:

        data.append(
            list(row)
        )


    table = Table(
        data,
        repeatRows=1
    )


    table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    0.5,
                    None
                ),

                (
                    "ALIGN",
                    (0,0),
                    (-1,-1),
                    "CENTER"
                )
            ]
        )
    )


    return table



# ----------------------------
# Generate PDF
# ----------------------------

def create_report():


    os.makedirs(
        REPORT_PATH,
        exist_ok=True
    )


    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4
    )


    styles = getSampleStyleSheet()


    content = []



    # =========================
    # Title Page
    # =========================

    content.append(
        Paragraph(
            "Quantitative Portfolio Optimization Report",
            styles["Title"]
        )
    )


    content.append(
        Spacer(1,30)
    )


    content.append(
        Paragraph(
            """
            Construction and evaluation of a maximum
            Sharpe ratio equity portfolio using
            Modern Portfolio Theory.
            """,
            styles["BodyText"]
        )
    )


    content.append(
        Spacer(1,30)
    )


    content.append(
        Paragraph(
            "By Noku Mushayakarara",
            styles["BodyText"]
        )
    )


    content.append(
        PageBreak()
    )



    # =========================
    # Methodology
    # =========================


    content.append(
        Paragraph(
            "1. Methodology",
            styles["Heading2"]
        )
    )


    methodology = """

    The portfolio was constructed using Modern Portfolio Theory.
    Historical stock returns were used to estimate expected
    returns and covariance. Portfolio weights were optimized
    by maximizing the Sharpe ratio.

    The resulting portfolio was evaluated through
    return, volatility, risk-adjusted performance measures
    and drawdown analysis.

    A benchmark portfolio was created using an equal-weight
    allocation across the same 17 stocks to determine whether
    optimization added value.

    """


    content.append(
        Paragraph(
            methodology,
            styles["BodyText"]
        )
    )


    content.append(
        Spacer(1,20)
    )



    # =========================
    # Performance Metrics
    # =========================


    content.append(
        Paragraph(
            "2. Portfolio Performance",
            styles["Heading2"]
        )
    )


    performance = pd.read_csv(
        f"{TABLE_PATH}/performance_table.csv"
    )


    content.append(
        create_table(
            performance
        )
    )


    content.append(
        Spacer(1,20)
    )



    # =========================
    # Benchmark Comparison
    # =========================


    content.append(
        Paragraph(
            "3. Benchmark Comparison",
            styles["Heading2"]
        )
    )


    benchmark = pd.read_csv(
        f"{TABLE_PATH}/portfolio_vs_benchmark.csv"
    )

    report= """

    The results reveal a clear trade-off between stability and raw performance. 
    The benchmark delivers a much higher annual return, yet this comes at the cost of 
    extreme volatility. Its annual volatility is nearly twenty times greater than that 
    of the optimized portfolio, making its returns highly unstable and unpredictable. 
    By contrast, the optimized portfolio achieves far lower volatility and smaller 
    drawdowns, offering a more consistent and resilient performance profile.

    Risk-adjusted measures further highlight this distinction. The optimized portfolio 
    records a stronger Sharpe ratio, indicating that it generates more return per unit 
    of risk than the benchmark. This suggests that, despite lower absolute returns, the 
    optimized portfolio is more efficient in balancing reward against risk. 
    Interestingly, the benchmark shows unusually high Sortino and Calmar ratios, which 
    may reflect calculation quirks or the disproportionate influence of its outsized 
    returns relative to downside risk. Nevertheless, these figures do not negate the 
    fact that the benchmark's volatility and drawdowns are significantly larger.

    Taken together, the comparison underscores the essence of portfolio optimization. It 
    is not about chasing the highest possible return, but about achieving a sustainable 
    balance between growth and risk. The optimized portfolio demonstrates that 
    stability, resilience, and efficiency can outweigh raw performance, especially for 
    investors who prioritize long-term risk management over short-term gains.

            """


    content.append(
        Paragraph(
            """
            The optimized portfolio is compared against
            an equal-weight benchmark consisting of the same
            securities.

            This comparison evaluates whether portfolio
            optimization improved risk-adjusted returns.
            """,
            styles["BodyText"]
        )
    )


    content.append(
        Spacer(1,10)
    )


    content.append(
        create_table(
            benchmark
        )
    )

    content.append(
    Spacer(1, 12)
)

    content.append(
    Paragraph(
        report,
        styles["BodyText"]
    )
)

    content.append(
    Spacer(1, 20)
)


    content.append(
        Spacer(1,20)
    )



    # =========================
    # Charts
    # =========================

    charts = [

        (
            "4. Portfolio Growth",
            "cumulative_returns.png"
        ),

        (
            "5. Drawdown Analysis",
            "drawdown.png"
        ),

        (
            "6. Portfolio Allocation",
            "portfolio_allocation.png"
        ),

        (
            "7. Efficient Frontier",
            "efficient_frontier.png"
        )

    ]



    for title, filename in charts:


        content.append(
            Paragraph(
                title,
                styles["Heading2"]
            )
        )


        img = Image(
            f"{FIGURE_PATH}/{filename}",
            width=400,
            height=250
        )


        content.append(
            img
        )


        content.append(
            Spacer(1,20)
        )



    # =========================
    # Conclusion
    # =========================


    content.append(
        Paragraph(
            "8. Conclusion",
            styles["Heading2"]
        )
    )


    conclusion = """

    This study demonstrated the application of quantitative portfolio optimization 
    techniques in constructing and evaluating an equity investment portfolio. 
    Using historical return data from seventeen South African listed companies, 
    a maximum Sharpe ratio portfolio was developed based on Modern Portfolio Theory 
    principles, where asset weights were optimized to achieve the most efficient 
    risk-adjusted return profile.

    The empirical results indicate that the optimized portfolio provided an improved 
    balance between return and risk compared with an equally weighted benchmark 
    portfolio. By incorporating the historical relationships between asset returns 
    through covariance estimation, the optimized portfolio was able to achieve a more 
    efficient allocation of capital across the selected securities. The comparison with 
    the equal-weight benchmark suggests that systematic portfolio construction and 
    diversification techniques can enhance investment outcomes by reducing unnecessary 
    exposure to individual securities while maintaining attractive return potential.

    From a wealth management perspective, the findings highlight the importance of 
    disciplined asset allocation rather than relying solely on individual security 
    selection. The optimized portfolio demonstrates how quantitative methods can assist 
    investment managers in making objective allocation decisions, managing portfolio 
    risk and improving risk-adjusted performance. Measures such as the Sharpe ratio, 
    Sortino ratio and maximum drawdown provide evidence that portfolio evaluation should 
    consider both return generation and downside risk management.

    However, the results should be interpreted within the limitations of the methodology.
    Portfolio optimization relies heavily on historical estimates of expected returns and 
    correlations, which may not remain stable in changing market environments. Market 
    conditions, economic cycles, liquidity constraints and investor objectives can 
    significantly influence future portfolio performance. Therefore, the optimized 
    portfolio should not be viewed as a guaranteed superior investment strategy, but 
    rather as a quantitative framework that supports informed portfolio decision-making.

    Overall, the analysis confirms that quantitative optimization techniques can provide 
    valuable tools for modern wealth management by enabling investors to construct 
    portfolios that are aligned with their desired risk-return objectives. Combining 
    mathematical optimization with professional judgement and continuous portfolio 
    monitoring remains essential for achieving sustainable long-term investment outcomes.
    """


    content.append(
        Paragraph(
            conclusion,
            styles["BodyText"]
        )
    )


    doc.build(
        content
    )


    print(
        f"Report created: {OUTPUT_FILE}"
    )



if __name__ == "__main__":

    create_report()