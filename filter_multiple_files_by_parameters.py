# base path related variables
basepath = r'.\Python_DA'
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

dfp_headers = paramlist[3]   # headers
# loop through the dataframe columns
for column_name, data in dfp_headers.items():
    # print data in the first 3 rows
    print(column_name, ':', data[0], data[1], data[2])

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
#print(list(paramlist_filtered[1].loc[ : , 'Product']))

# get the list of the column headers
#print(list(paramlist_filtered[1].columns))

# get one single row in a list
#print(list(paramlist_filtered[1].loc[0]))

# get the position of a value in the list of a row
#print(list(paramlist_filtered[1].loc[0]).index('640 Fax Machine'))

# get the position of a value in the list of a column
#print(list(paramlist_filtered[1].loc[ : , 'Product']).index('640 Fax Machine'))

## read the input file, clean, filter, translate and export it

df = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8')

exec(compile(source=open('week2_Clean_data2.py').read(), filename='week2_Clean_data2.py', mode='exec'))
df = df.drop(['index'], axis= 1)

# filter column to values are in the list
df = df[df['Product'].isin(products_to_be_filtered)]
#print(df)

# get the unique values in a column (without duplicates)
products_unique = list(df['Product'].unique())
#print(products_unique)

# extend our dataframe with the regions of the customers
dfp_regions = paramlist_filtered[2]
#print(dfp_regions)
# merge two dataframes
# one column name is common in both
# how:
#   left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
#   right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
#   outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
#   inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.
#   cross: creates the cartesian product from both frames, preserves the order of the left keys.
print(list(df['Customer'].unique()))
print(list(dfp_regions['Customer'].unique()))
df = pd.merge(df, dfp_regions, on= 'Customer', how= 'inner')
# we give two name, one for the left, another for the right dataframe
#df = pd.merge(df, dfp_regions, left_on= 'Customer', right_on= 'Client', how= 'inner')
#print(df)

# replace the English headers with German ones
dfp_headers = paramlist_filtered[3]
# add column values to list
oldheader_list = dfp_headers['Old header'].tolist()
newheader_list = dfp_headers['New header'].tolist()
# create dictionaries from the lists
header_dict = dict(zip(oldheader_list, newheader_list))
# translate headers based on the dictionary
df.columns = pd.Series(df.columns).replace(header_dict)

# # translate column values based on a dictionary
# header_dict2 = dict(zip(['North', 'East', 'South', 'West'], ['Nord', 'Ost', 'Süd', 'West']))
# df['Region'] = df['Region'].replace(header_dict2)
# print(df)

outputfile = inputfile.replace('.csv', '_cleaned_filtered.csv')
exec(compile(source=open('Export_to_csv.py').read(), filename='Export_to_csv.py', mode='exec'))



# beep
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)

# store the endtime
endtime = time.time()
# print runtime
print(runtime(starttime, endtime))

print('All source files cleaned!')