# import the pandas data analysis library
import pandas as pd
import os

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Input'
inputfile = 'Source1.csv'
outputfolder = 'Output'
outputfile = 'Revenues.csv'

#exec(compile(source=open('Read_csv.py').read(), filename='Read_csv.py', mode='exec'))
# read data from a csv file into a dataframe
df = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8')

exec(compile(source=open('week2_Clean_data2.py').read(), filename='week2_Clean_data2.py', mode='exec'))
#exec(compile(source=open('Write_csv.py').read(), filename='Write_csv.py', mode='exec'))

# reduce the dataframe to a specific column
df_products = df[['Product']]
# remove the duplicated
df_products = df_products.drop_duplicates()

# another possibility
# remove the fuplicated regarding a given column using the subset paramter
df_products2 = df.drop_duplicates(subset= ['Product'])
# reduce the dataframe to a specific column
df_products2 = df_products2[['Product']]


print(df_products)