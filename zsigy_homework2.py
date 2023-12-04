# Homework 2 - Week 2
# Created by István Gy. Zsély
# version 0.1
# For details look in the README.md file.

# import the pandas data analysis library
import pandas as pd
import os
import re

# file related variables
basepath = r'.\Python_DA\Homework2'

# Task 1
# the input folder is 'Input' and the input file is 'Orders_2011.csv'
inputfolder = 'Input'
inputfile = 'Orders_2011.csv'

# Task 2
# the output folder is 'Output'
outputfolder = 'Output'

# Task 10
# the output file must be named as the input one with the ending '_cleaned.csv'
outputfile = inputfile[ : len(inputfile)-4] + '_cleaned.csv'

# Task 3
# use the external program from Read_csv.py to read the input file
exec(compile(source=open('Read_csv.py').read(), filename='Read_csv.py', mode='exec'))

# Task 4
# remove the extra leading and tailing spacec from column 'Class'
df['Class'] = df['Class'].str.strip(' ')

# Task 5
# covert the type of column 'OederDate" to DATETIME
df['OrderDate'] = pd.to_datetime(df['OrderDate'], dayfirst = False)

# Task 6
# conversion of the data of column 'LineTotal' to float
# replace the comma decimal separator to dot
df['LineTotal'] = df['LineTotal'].str.replace(',', '.')
df['LineTotal'] = df['LineTotal'].astype(dtype = 'float64', errors = 'ignore')

# Task 7
# separate the Size from the date to day, month and year
df[['Product_name', 'Size']] = df['ProductName'].str.split(',', expand = True)
# replace the 'Black', 'Red' and 'Blue' "sizes" with '-'
df['Size'] = df['Size'].str.replace('Black', '-')
df['Size'] = df['Size'].str.replace('Red',   '-')
df['Size'] = df['Size'].str.replace('Blue',  '-')

print(df.iloc[250 : 280, : ])
#df['Year'] = df['Date'].dt.year

df['Size'].to_csv(basepath + '\\' + outputfolder + '\\' + 'Size.csv',
          index = False, sep = ';', encoding = 'utf-8')