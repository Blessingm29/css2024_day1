#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:31:54 2024

@author: blessingmkhonazi
"""

"""
Data frames
"""


fruits = ["apple", "banana", "orange", "grape", "kiwi"]
          
Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {'fruits' : fruits, 
               'sizes': Size_nm}

#df = data frame

import pandas as pd
df = pd.DataFrame(fruit_sizes)

print(df['fruits'])
print(df['sizes'])
print(df['sizes'].mean)


#Adding a new column


prices = [10.00, 12.50, 16.00, 23.00, 7.00]
df ['prices']= prices
df.drop(columns=["sizes"], inplace = True)
