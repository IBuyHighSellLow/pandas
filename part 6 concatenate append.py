# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:22:47 2019

@author: fjga6
"""

import pandas as pd

df1 = pd.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   )

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[6, 7, 6, 9],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   )

#print(pd.merge(df1,df2, on=['HPI','Int_rate']))

#df1.set_index('Year', inplace = True)
#df3.set_index('Year', inplace = True)

#joined = df1.join(df3)

#print(joined)
#how has either (left, right, outer, inner)
merged = pd.merge(df1, df3, on= 'Year', how= 'outer')

merged.set_index('Year', inplace= True)
print(merged)

