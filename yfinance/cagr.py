import yfinance as yf
import numpy as np


start_date = '2015-01-01'
end_date = '2021-12-31'
stock_data = yf.download('GOOGL', start_date, end_date)

#######   Cummalative Annual Growth Rate   #######
def cagr(data):
    df = data.copy()
    df["daily_return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1 + df["daily_return"]).cumprod()

    trading_days = 252
    n = len(df) / trading_days
    this_cagr = (df["cum_return"][-1] ** (1 / n)) - 1
    return this_cagr


print("CAGR: " + str(cagr(stock_data) * 100) + '%')
