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
# check the data dype of the columns
# print(df['Date'].dtype)
# print(df.dtypes)
# df['Date'] = df['Date'].astype('datetime64[ns]')
df['Date'] = pd.to_datetime(df['Date'], dayfirst = True)

# conversion of a column to numeric
# df['xxx'] = pd.to_numeric(df['xxx'], errors = 'coerce')
# conversion of the data of a column to float
# df['xxx'] = df['xxx'].astype(dtype = 'float64', errors = 'ignore')

# delete the Description column
df = df.drop(['Description'], axis = 1)
# delete multiple columns, e.g. Day, Month and Year
#df = df.drop(['Day', 'Month', 'Year'], axis = 1)
df2 = df.drop(columns = ['Day', 'Month', 'Year'])

# deleta row(s)
df2 = df.drop([1, 3, 4], axis = 0)

# filtering by the content of some column
df2 = df.drop(df.index[df['Product'] == '640 Fax Machine'])

# rename a single column
df2.rename(columns = {'Customer': 'Client'}, inplace = True)

# rename multiple columns
df2.rename(columns = {'Revenue': 'Sales', 'Salesperson': 'Salesclerk'}, inplace = True)

# reorder of the columns is only by referencing the column headers
df = df[['Customer', 'Product', 'Date', 'Revenue', 'Salesperson']]
# copy of the columns to a new dataframe is similar to this
df2 = df[['Customer', 'Product', 'Date', 'Revenue']]

# pick the values of a column out (removes it from the original dataframe!)
column_values = df.pop('Product')
# insert the values to a dataframe.       position, name, values
df.insert(0, 'Product', column_values)

# add a new, empty column
df.insert(0, 'Product2', '')
# adding a new column to the right: just set the value of a non-existing column header
# extraction of the information from a column of date type
# Warning: in case of the SettingWithCopyWarning use the following: pd.options.mode.chained_assignment = None
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# remove the unnecessary Produc2 column
df = df.drop(['Product2'], axis = 1)

# sort the rows of the dataframe by column
df = df.sort_values(by = ['Product'])
# sort in the descending order
df = df.sort_values(by = ['Product'], ascending = False)
# sorting for multiple columns, order of the columns matter!
df = df.sort_values(by = ['Product', 'Customer'])

# before sorting of a column having different types of data a conversion to string may be needed
# df['Product'] = df['Product'].astype(str)

# sor the data by the Date column
df = df.sort_values(by = ['Date'])

print(df)

