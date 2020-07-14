# AlgoTrading
Built over the lockdown while revising statistics concepts. It is a simple algorithm that gives long and short signals using Moving Average. 
We also use multiple linear regression to predict the open price of a stock in this case (AAPL) and based on it whether we long or short, we also compare the strategy to buy and hold strategy. 
The data used for the moving average strategy is 6 month daily historical data.
The data used for the multiple linear regression strategy is 10 year daily historical data

To collect data - will collect data for a list of stocks from yfinance 
6m - Data_6m.py
Annual - Data_1Y.py
10 year - Data_10.py 

Moving average - TradingStrategyBasic.py - Calculates 20 day and 50 day moving average, when MA50 > MA20 it gives a long signal. We also generate Bollinger bands to estimate the movement of the price. 

Risk Analysis - Strategy_Risk_1Y.py - Calculates VaR, probablity of 10 - 15% loss based on annual data 
Strategy_Risk_10Y.py - Calculated VaR, probability of 10 - 15% in a day, month, year using historical data of 10 year time period 

Regression:
MLR_stocks & MLR_stocks_tech - Multiple regression for calculating correlation and estimating open price for the next day - done for SPY and AAPL. 
algo_trading_strategy & algo_trading_strategy_tech - Evaluate whether the trading strategy based on multiple linear regression is effective and do we actually outperform a buy & hold strategy. Use Sharpe's ratio, Maximum Drawdown to verify if the strategy is profitable or not. 
