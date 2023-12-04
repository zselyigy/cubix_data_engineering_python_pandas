# Homework 2 - Week 2
# Created by István Gy. Zsély
# version 0.1

# import the pandas data analysis library
import pandas as pd
import os

# write out the README.md


# base path related variables
basepath = r'.\Python_DA\Homework2'
# Task 1
inputfolder = 'Input'
inputfile = 'Orders_2011.csv'
# Task 2
outputfolder = 'Output'
# Task 10
outputfile = inputfile[ : len(inputfile)-4] + '_cleaned.csv'

# Task 3
exec(compile(source=open('Read_csv.py').read(), filename='Read_csv.py', mode='exec'))

# Task 4
df['Class'] = df['Class'].str.replace('\s+', ' ', regex = True)
print(df['Class'])