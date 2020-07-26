# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:08:23 2020

@author: Dell
"""


import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
# hist = msft.history(period='1d', start='2015-1-1', end='2020-6-25')
# hist = msft.history(period="max")
hist = msft.history(period='1d', start='2019-1-1', end='2020-6-25')
hist
# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration
opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts










#if you want to use a proxy server for downloading data, use:

import yfinance as yf

msft = yf.Ticker("MSFT")

msft.history(..., proxy="PROXY_SERVER")
msft.get_actions(proxy="PROXY_SERVER")
msft.get_dividends(proxy="PROXY_SERVER")
msft.get_splits(proxy="PROXY_SERVER")
msft.get_balance_sheet(proxy="PROXY_SERVER")
msft.get_cashflow(proxy="PROXY_SERVER")
msgt.option_chain(..., proxy="PROXY_SERVER")

# To initialize multiple Ticker objects, use

import yfinance as yf

tickers = yf.Tickers('msft aapl goog')
# ^ returns a named tuple of Ticker objects

# access each ticker using (example)
tickers.msft.info
tickers.aapl.history(period="1mo")
tickers.goog.actions

# Fetching data for multiple tickers
import yfinance as yf
data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

# I’ve also added some options to make life easier :)

data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "SPY AAPL MSFT",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "ytd",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )



# pandas_datareader override
# If your code uses pandas_datareader and you want to download data faster, 
# you can “hijack” pandas_datareader.data.get_data_yahoo() method 
# to use yfinance while making sure the returned data is in the same format 
# as pandas_datareader’s get_data_yahoo().

from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")