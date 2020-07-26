# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:32:44 2020

@author: Dell
"""
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75


# Installation
# Install yfinance using pip:

# $ pip install yfinance --upgrade --no-cache-dir
# Install yfinance using conda:

# $ conda install -c ranaroussi yfinance

# CREATE FUNCTION TO GET AND TRANSFORM STOCK DATA 

def stock_summary_function(ticker):
    import yfinance as yf
    
    #define the ticker symbol
    tickerSymbol = ticker
    
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    
    #get the five-year historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2019-1-1', end='2020-6-25')
    
    #see your data
    tickerDf.head()
    
   
    
    #info on the company
    #tickerData.info
    
    #get event data for ticker
    #tickerData.calendar
    
    #get recommendation data for ticker
    #tickerData.recommendations
    
    
    
    # split time
    import datetime
    tickerDf['year']=0
    tickerDf['month']=0
    tickerDf['day']=0
    for i in range(0, len(tickerDf.index)):
        a = tickerDf.index[i]
        # format date time with local time
        tickerDf['year'][i] = datetime.datetime.strptime(str(a), "%Y-%m-%d  %X").year
        tickerDf['month'][i]= datetime.datetime.strptime(str(a), "%Y-%m-%d  %X").month
        tickerDf['day'][i]= datetime.datetime.strptime(str(a), "%Y-%m-%d  %X").day
    
   
    import pandas as pd
    import numpy as np
    
    
    years = np.unique(tickerDf['year']) # list object
    # can also write this way: years = list(np.unique(tickerDf['year'])) # list object
    # can also list item: years = [2019, 2020]
    date = []
    year = []
    month = []
    min_close = []
    max_close = []
    spread_close = []
    mean_high = []
    mean_low = []
    mean_vol = []
    for y in years:
        #mm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # list object
        for m in range(1, 13):
            # create date time format
            yyyy_mm = pd.to_datetime(str(y)+str('-')+str(m))
            date.append(yyyy_mm)
            year.append(y) # append year (i.e., 2019) 12 times
            month.append(m) # append month (i.e., 1) each time
            min_close_item = tickerDf[tickerDf.year.isin([y]) & tickerDf.month.isin([m])]['Close'].min()
            max_close_item = tickerDf[tickerDf.year.isin([y]) & tickerDf.month.isin([m])]['Close'].max()
            spread_close_item = max_close_item - min_close_item
            mean_high_item = tickerDf[tickerDf.year.isin([y]) & tickerDf.month.isin([m])]['High'].mean()
            mean_low_item = tickerDf[tickerDf.year.isin([y]) & tickerDf.month.isin([m])]['Low'].mean()
            mean_vol_item = tickerDf[tickerDf.year.isin([y]) & tickerDf.month.isin([m])]['Volume'].mean()
            print('date: ', date)
            print('min close: ', min_close_item)
            print('max close: ', max_close_item)
            print('spread close: ', spread_close_item)
            print('mean high: ', mean_high_item)
            print('mean low: ', mean_low_item)
            print('mean_vol: ', mean_vol_item)
            min_close.append(min_close_item)
            max_close.append(max_close_item)
            spread_close.append(spread_close_item)
            mean_high.append(mean_high_item)
            mean_low.append(mean_low_item)
            mean_vol.append(mean_vol_item)
    
    
    
    df_stock = pd.DataFrame({'date': date, 'year': year, 'month': month, 
                            'spread_close': spread_close,
                            'min_close': min_close, 'max_close': max_close,  
                            'mean_high': mean_high, 'mean_low': mean_low, 
                            'mean_vol': mean_vol})
    
    # make date index column
    df_stock = df_stock.set_index('date')
    return(df_stock)
################# END FUNCTION ##############
    



df = stock_summary_function(ticker = 'HD')


# graphing the stock summary information
from matplotlib import pyplot
# line time series
df.iloc[:, [2]].plot()
# using dash lines
pyplot.show()
    # more at https://machinelearningmastery.com/time-series-data-visualization-with-python/ 
import seaborn as sns
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(11, 4)})
# select multiple columns
df.iloc[:, 2:7].plot()
# selecting a single column or more, use list type []
#df_test.iloc[:, [2, 3]].plot()
pyplot.show()



