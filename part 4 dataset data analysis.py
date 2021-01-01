# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:13:06 2019

@author: fjga6
"""
import quandl
import pandas as pd

api_key = open('apikey.txt', 'r').read()

df = quandl.get('CMHC/HPPU50_BC', authoken= api_key)

#print(df.head())

friddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#this is a list:
#print(friddy_states)

#this is a dataframe
#print(friddy_states[0])

#this is a column
print(friddy_states[0][1])

for x in friddy_states[0][1]:
    print('CMHC/HPPU50_'+str(x))
    