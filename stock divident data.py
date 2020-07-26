# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:12:18 2020

@author: Dell
"""


# getting website
import requests
from bs4 import BeautifulSoup
### the url is the desired site that the web redirect too after log in
url='https://www.dividend.com/dividend-stocks/high-dividend-yield-stocks/#tm=3-high-yield-stocks&r=Webpage%231281&f_35=true&f_9_min=2&f_9_max=100&only=meta%2Cdata%2Cthead&page=1'
url='https://www.dividend.com/dividend-stocks/high-dividend-yield-stocks/#tm=3-high-yield-stocks&r=Webpage%231281&f_35=true&f_9_min=2&f_9_max=100&only=meta%2Cdata%2Cthead&page=2'
url='https://www.dividend.com/dividend-stocks/high-dividend-yield-stocks/#tm=3-high-yield-stocks&r=Webpage%231281&f_35=true&f_9_min=2&f_9_max=100&only=meta%2Cdata%2Cthead&page=3'
url='https://www.dividend.com/dividend-stocks/high-dividend-yield-stocks/#tm=3-high-yield-stocks&r=Webpage%231281&f_35=true&f_9_min=2&f_9_max=100&only=meta%2Cdata%2Cthead&page=4'
# last page
url='https://www.dividend.com/dividend-stocks/high-dividend-yield-stocks/#tm=3-high-yield-stocks&r=Webpage%231281&f_35=true&f_9_min=2&f_9_max=100&only=meta%2Cdata%2Cthead&page=73'
base_url='https://www.dividend.com/dividend-stocks/high-dividend-yield-stocks/#tm=3-high-yield-stocks&r=Webpage%231281&f_35=true&f_9_min=2&f_9_max=100&only=meta%2Cdata%2Cthead&page='

# create a url list to crawl
stc_url_list=[]
for i in range(1, 74):
    stc_url_item=str(base_url+str(i))
    stc_url_list.append(stc_url_item)
# first ulr item starts from index = 0
stc_url_list[1]

# store all pages 
#page_storage=[]
stock_data=[]
for url_index in range(0, 2):
    url=stc_url_list[url_index]
    r = requests.get(url)
    html_contents = r.text
    html_soup = BeautifulSoup(html_contents, 'html.parser')
        
# it starts iterate from page 1 to the last page to get the data
    stock_tables = html_soup.find_all('table', class_='m-0 n-sticky-header-table p-0 page--text__md t-bg-white table-bordered table-module xl:t-w-full')
    
    for table in stock_tables:
        headers = []
        # this includes all the rows: row for header and row for data
        rows = table.find_all('tr')
        # Start by fetching the header cells from the first row to determine
        # the field names
        # it will find one by one
        # that's why we need to use append to append values
        for header in table.find('tr').find_all('th'):
            # strip() is used to trim leading and trailing white space and tab
            headers.append(header.text.strip())
            # Then go through all the rows except the first one
            # because the first one is the header row
        for row in rows[1:]:
            values = []
                # And get the column cells, the first one being inside a th-tag
            for col in row.find_all(['th','td']):
                    values.append(col.text)
            if values:
                    # each header column will be given 1 its a value
                    # this is being done from col index 1 to index len(headers)-1
                    # note that col 0 is blank; so no need to get it. 
                    stock_dict = {headers[i]: values[i] for i in range(1, len(headers), 1)}
                    stock_data.append(stock_dict)
# Show the results
# for x in stock_data:
#     print(x)
# not working as intended
import pandas as pd
df=pd.DataFrame(stock_data)



#   GET PAGES ONE BY ONE

stock_data=[]
url='https://www.dividend.com/dividend-stocks/#tm=3-top-100&r=Webpage%231282&only=meta%2Cdata%2Cthead'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
        
# it starts iterate from page 1 to the last page to get the data
stock_tables = html_soup.find_all('table', class_='m-0 n-sticky-header-table p-0 page--text__md t-bg-white table-bordered table-module xl:t-w-full')

for table in stock_tables:
    headers = []
    # this includes all the rows: row for header and row for data
    rows = table.find_all('tr')
    # Start by fetching the header cells from the first row to determine
    # the field names
    # it will find one by one
    # that's why we need to use append to append values
    for header in table.find('tr').find_all('th'):
        # strip() is used to trim leading and trailing white space and tab
        headers.append(header.text.strip())
        # Then go through all the rows except the first one
        # because the first one is the header row
    for row in rows[1:]:
        values = []
            # And get the column cells, the first one being inside a th-tag
        for col in row.find_all(['th','td']):
                values.append(col.text)
        if values:
                # each header column will be given 1 its a value
                # this is being done from col index 1 to index len(headers)-1
                # note that col 0 is blank; so no need to get it. 
                stock_dict = {headers[i]: values[i] for i in range(1, len(headers), 1)}
                stock_data.append(stock_dict)
                
# get another page
url='https://www.dividend.com/dividend-stocks/high-dividend-yield-stocks/#tm=3-high-yield-stocks&r=Webpage%231281&f_35=true&f_9_min=2&f_9_max=100&only=meta%2Cdata%2Cthead&page=1'
r2 = requests.get(url)
html_contents2 = r2.text
html_soup2 = BeautifulSoup(html_contents2, 'html.parser')
        
# it starts iterate from page 1 to the last page to get the data
stock_tables2 = html_soup2.find_all('table', class_='m-0 n-sticky-header-table p-0 page--text__md t-bg-white table-bordered table-module xl:t-w-full')

for table in stock_tables2:
    headers2 = []
    # this includes all the rows: row for header and row for data
    rows = table.find_all('tr')
    # Start by fetching the header cells from the first row to determine
    # the field names
    # it will find one by one
    # that's why we need to use append to append values
    for header2 in table.find('tr').find_all('th'):
        # strip() is used to trim leading and trailing white space and tab
        headers2.append(header2.text.strip())
        # Then go through all the rows except the first one
        # because the first one is the header row
    for row in rows[1:]:
        values = []
            # And get the column cells, the first one being inside a th-tag
        for col in row.find_all(['th','td']):
                values.append(col.text)
        if values:
                # each header column will be given 1 its a value
                # this is being done from col index 1 to index len(headers)-1
                # note that col 0 is blank; so no need to get it. 
                # use the previous headings
                stock_dict = {headers[i]: values[i] for i in range(1, len(headers), 1)}
                stock_data.append(stock_dict)
                
# Show the results
# for x in stock_data:
#     print(x)
# not working as intended
df=pd.DataFrame(stock_data)
df.to_csv(r'C:\Users\Dell\Documents\00_Python Programming\practice data\2020_stock_data.csv', index=False)
