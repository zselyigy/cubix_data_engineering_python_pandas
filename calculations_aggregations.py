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

## final section - notification sound, runtime, final message to user
# beep
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)

# store the endtime
endtime = time.time()
# print runtime
print(runtime(starttime, endtime))

print('All source files cleaned, filtered, and exported!')