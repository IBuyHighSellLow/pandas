# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 21:49:09 2019

@author: fjga6
"""

import pandas as pd

df= pd.read_csv('NASDAQOMX-XNDXT25E.csv')

print(df.head())

df.set_index('Trade Date', inplace=True)

df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv', index_col= 0)
print(df.head())

