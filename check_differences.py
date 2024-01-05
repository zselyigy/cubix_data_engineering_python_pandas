## inital section - base data, necessary modules and functions

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Output\\All periods'
inputfile = 'Revenues_all_periods2.csv'
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


# replace NaN values to any value in a column
df['Unit price'] = df['Unit price'].fillna(0)
print(paramlist[0])


# add the missing items to the parameter sheet
if len(missingproducts) > 0:
    # calculation of the last row number in Excel
    lastrow_excel = paramlist[0].shape[0] + 1

    # import the openpyxl
    import openpyxl

    # load the Excel workbook
    paramfile_withpath = paramfolderpath + '\\' + paramfile
    wb = openpyxl.load_workbook(paramfile_withpath)
    # define ws as the appropriate worksheet of the Excel workbook
    ws = wb[paramfile_sheet]

    # add the missing items to the parameter sheet
    i = 0
    # for all items in missing products list
    for product in missingproducts:
        i += 1
        # write the data into the specific cells of the Excel sheet
        ws.cell(row = lastrow_excel + i, column= 1).value = product

    # save the Excel files (it also closes it)
    wb.save(paramfile_withpath)

## final section - notification sound, runtime, final message to user
# beep
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)

# store the endtime
endtime = time.time()
# print runtime
print(runtime(starttime, endtime))

if len(missingproducts) > 0:
    print('Missing products added to the parameter table!')
    print(missingproducts)
else:
    print('No missing products were found in the parameter table!')