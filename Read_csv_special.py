# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Output\\Filtered'
inputfile = 'Source1_cleaned_filtered.csv'

import pandas as pd
columnlist = ['Product', 'Customer', 'Date', 'Revenue']
rows_to_read = 10
converter_formula = {'Date': lambda x: x.replace('-', '')}

# read data from csv file into a dataframe
df = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8',
                 usecols= columnlist, nrows= rows_to_read, converters= converter_formula)
print(df)