# Portfolio Optimization and Backtesting using Python

## Overview

This project implements a complete quantitative portfolio optimization framework using historical stock data from the Johannesburg Stock Exchange (JSE). It demonstrates the end-to-end workflow of constructing an optimized equity portfolio, evaluating its performance and comparing it with the JSE All Share Index (ALSI).

The project applies Modern Portfolio Theory (MPT) by constructing both the Minimum Variance Portfolio and the Maximum Sharpe Ratio Portfolio. Portfolio performance is evaluated through backtesting, drawdown analysis and benchmark comparison.

---

## Objectives

- Collect and clean historical JSE stock price data
- Calculate simple and logarithmic returns
- Estimate expected returns and covariance matrices
- Apply covariance shrinkage techniques
- Construct optimal portfolios
- Simulate the Efficient Frontier
- Backtest portfolio performance
- Compare performance against the JSE All Share Index
- Produce professional financial visualizations

---

## Features

### Data Processing

- Historical price download
- Data cleaning
- Missing value handling
- Adjusted closing prices
- Simple returns
- Log returns

### Risk Analysis

- Asset descriptive statistics
- Correlation matrix
- Covariance matrix
- Shrunk covariance matrix

### Portfolio Optimization

- Expected return estimation
- Minimum Variance Portfolio
- Maximum Sharpe Ratio Portfolio
- Efficient Frontier simulation

### Backtesting

- Portfolio returns
- Cumulative returns
- Maximum Drawdown
- Drawdown analysis

### Visualization

- Correlation Heatmap
- Efficient Frontier
- Portfolio Weight Allocation
- Drawdown Plot
- Portfolio vs JSE ALSI Performance

---

## Project Structure

```
portfolio_optimization/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── figures/
│
├── src/
│   ├── data/
│   ├── optimization/
│   ├── risk/
│   ├── backtesting/
│   ├── visualization/
│   └── utils/
│
├── requirements.txt
├── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- yfinance

---

## Portfolio Optimization Methodology

The optimization process follows these steps:

1. Download historical JSE stock prices.
2. Clean and preprocess the dataset.
3. Compute daily returns.
4. Estimate expected returns.
5. Estimate covariance matrix.
6. Apply covariance shrinkage.
7. Generate thousands of random portfolios.
8. Compute:

   - Expected Return
   - Portfolio Volatility
   - Sharpe Ratio

9. Identify:

   - Minimum Variance Portfolio
   - Maximum Sharpe Ratio Portfolio

10. Backtest the optimized portfolio.

---

## Performance Evaluation

The project evaluates portfolio performance using:

- Expected Return
- Portfolio Volatility
- Sharpe Ratio
- Maximum Drawdown
- Cumulative Returns

The optimized portfolio is also compared against the Johannesburg Stock Exchange All Share Index (JSE ALSI).

---

## Generated Visualizations

The project produces the following figures:

- Correlation Heatmap
- Efficient Frontier
- Minimum Variance Portfolio Weights
- Maximum Sharpe Portfolio Weights
- Portfolio Drawdown
- Portfolio vs JSE ALSI Performance

---

## Installation

Clone the repository

```bash
git clone https://github.com/Javari-26/portfolio_optimization.git
```

Navigate to the project

```bash
cd portfolio_optimization
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the scripts in the following order:

1. Download data
2. Clean data
3. Compute returns
4. Calculate statistics
5. Estimate covariance
6. Optimize portfolio
7. Backtest portfolio
8. Generate visualizations

---

## Example Outputs

The project generates:

- Efficient Frontier
- Portfolio Allocation Charts
- Correlation Heatmap
- Drawdown Plot
- Portfolio vs Benchmark Comparison

---

## Future Improvements

Possible future enhancements include:

- Black-Litterman Portfolio Optimization
- Risk Parity Portfolio
- CVaR Optimization
- Rolling Window Optimization
- Transaction Cost Modeling
- Portfolio Rebalancing Strategies
- Factor Models (Fama-French)
- Machine Learning Return Forecasting

---

## Author

Nokutenda Mushayakarara

Bachelor of Science (Honours) in Financial Mathematics (2026)

University of Zimbabwe

Interested in:

- Quantitative Finance
- Debt Structuring, LBOs, M&As
- Portfolio Management
- Financial Risk Management
- Algorithmic Trading
- Data Science

---

