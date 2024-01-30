#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:45:37 2024

@author: blessingmkhonazi
"""

"""
Storing data in python
1. Lists
2. Dictionaries
3. Data Frames- specific to pandas
"""
import pandas
file = pandas.read_csv("Country_data.csv")

print (file)

age1 = 30
age2 = 25
age3 = 29
age = [30,25,29,46,22]

#Lists - square brackets for variables in a list format

print (age)

#To access value (for example, age 0 due to indexing)
print(age[0])
print(age[2])

#To print the minimum
print (min(age))

#to print the sum 
print(sum(age))

#To print length
print(len(age))

#To print average
print(sum(age)/len(age))

# Storing Text
#C2 = M
#C3 = M
#C4 = F

C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]

gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])