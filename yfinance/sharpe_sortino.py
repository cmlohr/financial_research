import yfinance as yf
import numpy as np


start_date = '2015-01-01'
end_date = '2021-12-31'
trading_days = 252
stock_data = yf.download('GOOGL', start_date, end_date)


######## CAGR ANN VOL required for Sharpe & Sortino ##########
def cagr(data):
    df = data.copy()
    df["daily_return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1 + df["daily_return"]).cumprod()
    n = len(df) / trading_days
    this_cagr = (df["cum_return"][-1] ** (1 / n)) - 1
    return this_cagr

def annualized_volatility(data):
    df = data.copy()
    df["daily_return"] = df["Adj Close"].pct_change()
    vol = df["daily_return"].std() * np.sqrt(trading_days)
    return vol
################################################################



#######   Sharpe & Sortino Ratio Begin   #######

def sharpes_ratio(data, rf):
    df = data.copy()
    sharpe = (cagr(df)-rf) / annualized_volatility(df)
    return sharpe

print("Sharpe Ratio: " + str(sharpes_ratio(stock_data, 0.03)))

print("############################################################")

def sortino_ratio(data, rf):
    df = data.copy()
    df["daily_return"] = df["Adj Close"].pct_change()
    df["daily_return"] = np.where(df["daily_return"] < 0, df["daily_return"], 0)
    negative_vol = df["daily_return"].std() * np.sqrt(trading_days)
    sortino = (cagr(df)-rf) / negative_vol
    return sortino

print("Sortino Ratio: " + str(sortino_ratio(stock_data,0.03)))

