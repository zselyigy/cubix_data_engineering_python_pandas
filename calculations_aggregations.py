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
df['Sold quantuty'] = df['Revenue'] / df['Unit price']
print(df)

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