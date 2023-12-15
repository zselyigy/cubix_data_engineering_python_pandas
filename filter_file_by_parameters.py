# base path related variables
basepath = r'.\Python_DA'
inputfile = 'Source1.csv'
outputfolder = 'Output\\Filtered'

# parameter related data
paramfolderpath = r'.\Python_DA'
paramfile = 'Parameters.xlsx'
paramfile_sheet = 'Parameter tables'

usedcolumnlist = ['A:B', 'D:E', 'G:H', 'J:L']
paramlist = []

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

import read_parameters_callable as rp

# read the parameter file
paramlist = rp.read_parameters(paramfolderpath, paramfile, paramfile_sheet, usedcolumnlist)

# # # get the input folder path from the paramlist
# # df = paramlist[0]
# # filter a column on substring (contain) and put it to a new dataframe
# #df2 = df[ df['Input file'].str.contains(inputfile)]
# # filter a column on substring with exact match and put it to a new dataframe
# df2 = df[ df['Input file'] == inputfile]
# print(df2)

# get the paramters for the corresponding input file
paramlist_filtered = []
for myparamtable in paramlist:
    if 'Input file' in myparamtable.columns:        # we filter only the rows corresponds to out current input file
        df = myparamtable
        df2 = df[ df['Input file'] == inputfile]    # keep only the appropriate rows
        df2 = df2.reset_index(drop = True)          # reset the index after filtering
        paramlist_filtered.append(df2)
    else:
        paramlist_filtered.append(myparamtable)     # this case we append the input file independent table
# print(paramlist_filtered)

# create the input folder path
inputfolder = paramlist_filtered[0]['Input folder path'][0]

# put the products to be filtered to a list
products_to_be_filtered = paramlist_filtered[1]['Product'].tolist()
#print(products_to_be_filtered)
# put the products to be filtered to a list - version 2
print(list(paramlist_filtered[1].loc[ : , 'Product']))

# get the list of the column headers
print(list(paramlist_filtered[1].columns))

# get one single row in a list
print(list(paramlist_filtered[1].loc[0]))

# get the position of a value in the list of a row
print(list(paramlist_filtered[1].loc[0]).index('640 Fax Machine'))

# get the position of a value in the list of a column
print(list(paramlist_filtered[1].loc[ : , 'Product']).index('640 Fax Machine'))

## read the input file, clean, filter, translate and export it

df = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8')

exec(compile(source=open('week2_Clean_data2.py').read(), filename='week2_Clean_data2.py', mode='exec'))
df = df.drop(['index'], axis= 1)

# filter column to values are in the list
df = df[df['Product'].isin(products_to_be_filtered)]

# get the unique values in a column (without duplicates)
products_unique = list(df['Product'].unique())
print(products_unique)
exec(compile(source=open('Write_csv.py').read(), filename='Write_csv.py', mode='exec'))

# create the dimension tables, too
exec(compile(source=open('create_dimension_tables_callable_withlists.py').read(), filename='create_dimension_tables_callable_withlists.py', mode='exec'))


# beep
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)

# store the endtime
endtime = time.time()
# print runtime
print(runtime(starttime, endtime))

print('All source files cleaned!')