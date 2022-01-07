import yfinance as yf
import numpy as np

start_date = '2015-01-01'
end_date = '2021-12-31'
trading_days = 252
stock_data = yf.download('GOOGL', start_date, end_date)

################    CAGR Required    ############

def cagr(data):
    df = data.copy()
    df["daily_return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1 + df["daily_return"]).cumprod()


    n = len(df) / trading_days
    this_cagr = (df["cum_return"][-1] ** (1 / n)) - 1
    return this_cagr


print("CAGR: " + str(cagr(stock_data) * 100) + '%')
##################################################





##################    CALMAR    ##################
def max_drawdown(data):
    df = data.copy()
    df["daily_return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1 + df["daily_return"]).cumprod()
    df['cum_max'] = df['cum_return'].cummax()
    df['drawdown'] = df['cum_max'] - df['cum_return']
    df['drawdown_pct'] = df['drawdown'] / df['cum_max']
    max_dd = df['drawdown_pct'].max()
    return max_dd

def calmar_ratio(data, rf):
    df = data.copy()
    calmar = cagr(df) / max_drawdown(df)
    return calmar

print("Calmar Ratio: " + str(calmar_ratio(stock_data, 0.03)))

