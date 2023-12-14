# import the pandas data analysis library
import pandas as pd
import os

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Input'
inputfile = 'Source1.csv'
outputfolder = 'Output'
outputfile = 'Revenues.csv'

exec(compile(source=open('Read_csv.py').read(), filename='Read_csv.py', mode='exec'))
# print(df.to_string())   # prints the whole dataframe
exec(compile(source=open('week2_Clean_data2.py').read(), filename='week2_Clean_data2.py', mode='exec'))
exec(compile(source=open('Write_csv.py').read(), filename='Write_csv.py', mode='exec'))
