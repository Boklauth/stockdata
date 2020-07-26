# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:41:25 2020

@author: Dell
"""


import yfinance as yf
    
#define the ticker symbol
tickerSymbol = 'FSLY'

tickerData = yf.Ticker(tickerSymbol)

#get the five-year historical prices for this ticker
tickerDf = tickerData.history(period='5d', interval= "1m", start='2020-1-1', end='2020-6-26')

#see your data
tickerDf.head()




# download data
# Valid intervals: 
# minutes [1m, 2m, 5m, 15m, 30m, 60m, 90m] 
# hour: [1h]
# day: [1d, 5d]
# week: [1wk]
# month: [1mo, 3mo]
#get data on this ticker
temp_df = yf.download(tickers="INO", period="6mo", interval="60m")
temp_data.head()


monthly_data = yf.download(tickers="FSLY", period="6mo", interval="60m")    
monthly_data.head()

import datetime
temp_df['year']=0
temp_df['month']=0
temp_df['day']=0
for i in range(0, len(tickerDf.index)):
     a = tickerDf.index[i]
     # format date time with local time
     temp_df['year'][i] = datetime.datetime.strptime(str(a), "%Y-%m-%d  %X").year
     temp_df['month'][i]= datetime.datetime.strptime(str(a), "%Y-%m-%d  %X").month
     temp_df['day'][i]= datetime.datetime.strptime(str(a), "%Y-%m-%d  %X").day
        
test = temp_df.index[0]
type(test)

tz_aware = test.tz_convert(tz='America/New_York')
tz_aware2 = tz_aware.tz_convert(tz=None)

test_result=datetime.datetime.strptime(str(test), "%Y-%m-%d T%H:%M:%S %UTC").year

datetime.datetime.utcnow()
datetime.datetime.utcnow().isoformat()
datetime.datetime.utcnow().isoformat() + "Z"

temp_df.index.datetime.tz_localize(None)

########

data = "2019-10-22T00:00:00.000-05:00"
result1 = datetime.datetime.strptime(data[0:19],"%Y-%m-%dT%H:%M:%S")
result2 = datetime.datetime.strptime(data[0:23],"%Y-%m-%dT%H:%M:%S.%f")
result3 = datetime.datetime.strptime(data[0:9], "%Y-%m-%d")
###
import pytz
timestring = "2017-05-30T23:51:03Z"

# Create datetime object
d = datetime.datetime.strptime(timestring, "%Y-%m-%dT%H:%M:%SZ")
print(d.tzinfo) # Return time zone info
print(d.strftime("%d.%m.%y %H:%M:%S"))

# Set the time zone to 'Europe/Paris'
d = pytz.timezone('Europe/Paris').localize(d)
print(d.tzinfo) # Return time zone info
# Transform the time to UTC
d = d.astimezone(pytz.utc)
print(d.tzinfo) # Return time zone info
print(d.strftime("%d.%m.%y %H:%M:%S"))
#####

timestring= str(temp_df.index[1])
# Create datetime object
d = datetime.datetime.strptime(timestring, "%Y-%m-%dT%X-%I").localize(d)
print(d.tzinfo) # Return time zone info
print(d.strftime("%d.%m.%y %H:%M:%S"))

# Set the time zone to 'Europe/Paris'
d = pytz.timezone('Europe/Paris').localize(d)
print(d.tzinfo) # Return time zone info
# Transform the time to UTC
d = d.astimezone(pytz.utc)
print(d.tzinfo) # Return time zone info
print(d.strftime("%d.%m.%y %H:%M:%S"))

###############
# Returns unix timestamp for current time

# Get datetime object in local time
d = datetime.datetime.fromtimestamp(int(timestring))
# Return unix timestamp from datetime object
timestamp = d.timestamp()

