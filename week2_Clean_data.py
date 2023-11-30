# import the pandas data analysis library
import pandas as pd

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Input'
inputfile = 'Source1.csv'
outputfolder = 'Output'
outputfile = 'Revenues.csv'

# read data from a csv file into a dataframe
df = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8')
# print the number of rows and columns, the total number of cells and the column titles of the dataframe
# print(df.shape, df.size, df.columns)

# capitalize each word in the Sperson column.
df['Salesperson'] = df['Salesperson'].str.title()

# # remove the leading and tailing spaces from Customer column
# df['Customer'] = df['Customer'].str.strip(' ')
# print(df['Customer'][0])

# remove the unnecessary spaser from Customer column
df['Customer'] = df['Customer'].str.replace('\s+', ' ', regex = True)

# separate the product name and the date from the Description column
df[['Product', 'Date']] = df['Description'].str.split(' / ', expand = True)
# split the date to day, month and year
df[['Day', 'Month', 'Year']] = df['Date'].str.split('.', expand = True)
print(df)