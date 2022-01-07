import yfinance as yf
import numpy as np


start_date = '2015-01-01'
end_date = '2021-12-31'
stock_data = yf.download('GOOGL', start_date, end_date)

#######   Annual Volatility   #######
def annualized_volatility(data):
    df = data.copy()
    df["daily_return"] = df["Adj Close"].pct_change()
    vol = df["daily_return"].std() * np.sqrt(252)
    return vol


print("Annualized Volatility: " + str(annualized_volatility(stock_data) * 100) + '%')
