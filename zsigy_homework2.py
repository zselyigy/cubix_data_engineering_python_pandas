# Homework 2 - Week 2
# Created by István Gy. Zsély
# version 0.2
# For details look in the README.md file.

# import the pandas data analysis library
import pandas as pd
import os

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
# separate the Size from the product name
df[['Product_name', 'Size']] = df['ProductName'].str.split(', ', expand = True)
# we do not need the original, uncleaned ProductName column
df = df.drop(['ProductName'], axis = 1)
# replace the 'Black', 'Red' and 'Blue' "sizes" with '-'
pattern = r'\b(?:Black|Red|Blue)\b'
df['Size'] = df['Size'].str.replace(pattern, '-', regex = True)
# same with list:
# colorlist = ['Black', 'Blue', 'Red']
# df['Size'] = df['Size'].replace(colorlist, '-')

# Task 8
# create a dimension table from column Size
df_sizes = df[['Size']]
# sort the content in alphabetical order
df_sizes = df_sizes.sort_values(by = ['Size'])
# reset the index
df_sizes = df_sizes.reset_index(drop = True)
# insert the ID column to the first place using the df indexes
df_sizes.insert(0, 'SizeID', df_sizes.index + 1)
# exporting for test purposes only
# df_sizes.to_csv(basepath + '\\' + outputfolder + '\\' + 'Size.csv',
#             index = False, sep = ';', encoding = 'utf-8')
# write it out in terminal
print(df_sizes)


# Task 9
# sort the df dataframe by “OrderDate” and “Country”
df = df.sort_values(by = ['OrderDate', 'Country'])
# reset the index
df = df.reset_index(drop = False)

# Task 10
# export the df dataframe to csv using the Export_to_csv.py code
exec(compile(source=open('Export_to_csv.py').read(), filename='Export_to_csv.py', mode='exec'))

# Task 11
# Markdown description is in the zsigy_homework2_README.md file.

# Task 12
# final message to the user
print('All tasks are finished in week 2 Homework 2.')