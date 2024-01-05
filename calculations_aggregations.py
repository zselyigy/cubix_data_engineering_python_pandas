## inital section - base data, necessary modules and functions

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Output\\All periods'
inputfile = 'Revenues_all_periods.csv'
outputfolder = 'Output\\Aggregations'
outputfile = 'Revenues_all_periods_aggregated.csv'


# parameter related data
paramfolderpath = r'.\Python_DA'
paramfile = 'Product unit prices.xlsx'
paramfile_sheet = 'Prices'

usedcolumnlist = ['A:B']
paramlist = ['Product name']

# import modules
import pandas as pd, os, winsound, time

# define a function sor the calculation of runtime in a string with a specific format
def runtime(start, end):
    hour, remainder = divmod(end - start, 3600)
    minute, second = divmod(remainder, 60)
    return 'Runtime {:0>2}:{:0>2}:{:05.2f}'.format(int(hour), int(minute), second)

# store the starttime
starttime = time.time()

# create the output folder
try:
    os.mkdir(basepath + '\\' + outputfolder)
except:
    pass

import pandas_utility_functions as pu       # Module of utility functions used instead of direct execution of py files.

# read the parameter file
paramlist = pu.read_parameters(paramfolderpath, paramfile, paramfile_sheet, usedcolumnlist)


## main section - filter, clean files etc.
# read the main source file
df = pu.read_csv(basepath, inputfolder, inputfile)

# merge the two dataframes
df = pd.merge(df, paramlist[0], left_on='Product', right_on='Product name', how= 'left')
# calculate the sold quantity
df['Sold quantity'] = df['Revenue'] / df['Unit price']

# find missing values in a column
# find the rows where the 'Product name' is missing and put the corresponding value from the 'Product' column to the list
missingproducts = list(df.loc[df['Product name'].isnull(), 'Product'])
# remove the duplicates
missingproducts = list(dict.fromkeys(missingproducts))
print('Missing products:', missingproducts)

# find the rows where the 'Unit price' is missing and put the corresponding value from the 'Product' column to the list
missingprices = list(df.loc[df['Unit price'].isnull(), 'Product'])
# remove the duplicates
missingprices = list(dict.fromkeys(missingprices))
print('Missing unit prices:', missingprices)

# aggregate functions for column values
average_qty = df['Sold quantity'].mean()
min_qty = df['Sold quantity'].min()
max_qty = df['Sold quantity'].max()
count_qty = df['Sold quantity'].count()
sum_qty = df['Sold quantity'].sum()

print(average_qty, min_qty, max_qty, count_qty, sum_qty)

# aggregate functions for column values
average_rev = df['Revenue'].mean()
min_rev = df['Revenue'].min()
max_rev = df['Revenue'].max()
count_rev = df['Revenue'].count()
sum_rev = df['Revenue'].sum()

print(average_rev, min_rev, max_rev, count_rev, sum_rev)

# aggregating for rows
columnlist = ['Revenue', 'Unit price', 'Sold quantity']
df['Dummy total'] = df[columnlist].sum(axis= 1)
df['Dummy average'] = df[columnlist].mean(axis= 1)
# delete the two new columns since they are just for practicing purposes + the 'Product name'
df = df.drop(['Dummy total', 'Dummy average', 'Product name'], axis= 1)

# calculate ranges for column values
# insert a new column
df['Sold quantity range'] = df['Product']
# change the values in this new column to the desired ones
df.loc[df['Sold quantity'] >= average_qty, 'Sold qunatity range'] = 'Above average'
df.loc[df['Sold quantity'] < average_qty, 'Sold qunatity range'] = 'Belos average'

# import numpy library, which is used for working with arrays, matrices etc.
import numpy as np
# create a pivot table (both the columns and rows have header)
# values: the values in the table, index: rows, columns: columns, aggfunc: aggregation values, fill_value: fill the missing vlues
pivot_sum_rev = pd.pivot_table(df, values= 'Revenue', index= ['Customer'], columns= ['Product'], aggfunc= np.sum, fill_value= 0)
print(pivot_sum_rev)

# create a stacked column chart
import matplotlib.pyplot as plt
pivot_sum_rev.plot(kind= 'bar', stacked= True)
pivot_sum_rev.plot(kind= 'barh', stacked= True)
plt.show()

# crate another pivot table
pivot_sum_rev2 = pd.pivot_table(df, values= 'Revenue', index= ['Product'], aggfunc= np.sum)
pivot_sum_rev2.plot(kind= 'line', figsize= (15, 5))
plt.show()

## final section - notification sound, runtime, final message to user
# beep
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)

# store the endtime
endtime = time.time()
# print runtime
print(runtime(starttime, endtime))

print('All source file analyzed!')