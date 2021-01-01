# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:10:26 2019

@author: fjga6
"""
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
print(plt.style.available)

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,65,34],
             'Bounce_rate':[63,42,55,77,54,66]}

df = pd.DataFrame(web_stats)
'''
print(df)
print(df.head())
print(df.tail())
print(df.tail(2))

print(df.set_index('Visitors'))
'''
#df = df.set_index('Day')
#print(df.head())


