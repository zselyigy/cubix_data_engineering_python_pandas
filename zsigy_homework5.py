# Homework 5 - Week 5
# Created by István Gy. Zsély
# version 0.1
# For details look in the README.md file. (task 5)

# import modules
import pandas_utility_functions as pu       # Module of utility functions used instead of direct execution of py files.
import pandas as pd, os, winsound, time
from icecream import ic                     # a nice library for the replacement of print and more

# store the starttime
starttime = time.time()

# base path related variables
basepath = r'.\Python_DA\Homework5'
outputfolder = 'Output'

# task 1 Read the parameter tables from “Parameters_Homework5.xlsx”
# parameter related data
paramfolderpath = r'.\Python_DA\Homework5'
paramfile = 'Parameters_Homework5.xlsx'
paramfile_sheet = 'Parameter tables'
usedcolumnlist = ['A:B', 'D:E', 'G:H', 'J:K', 'M:O']
paramlist = []

# read the parameter file
paramlist = pu.read_parameters(paramfolderpath, paramfile, paramfile_sheet, usedcolumnlist)

# task 3 The input folder paths of the input files are in the 1st parameter table
# loop through the rows of this table to do the following subtasks on each input file
for row_index, data in paramlist[0].iterrows():
    inputfolder = data['Input folder path']
    inputfile = data['Input file']

    # task 3.a Filter the parameter dataframes to input file (paramlist -> paramlist_filt).
    paramlist_filt = []
    for myparamtable in paramlist:
        if 'Input file' in myparamtable.columns:        # we filter only the rows corresponds to out current input file
            df = myparamtable
            df2 = df[ df['Input file'] == inputfile]    # keep only the appropriate rows
            df2 = df2.reset_index(drop = True)          # reset the index after filtering
            paramlist_filt.append(df2)
        else:
            paramlist_filt.append(myparamtable)     # this case we append the input file independent table
    # ic(paramlist_filt)                     # check if the parameter table filtering works well

    # task 3.b Read the input file from its input folder path
    inputfolder = inputfolder[inputfolder.find('Input') : ]    # I work with relative paths, so the paths in the parameter file had to be cut.
    df = pu.read_csv(basepath, inputfolder, inputfile)

    # task 3.c Use the “Clean_order_data.ipynb” external program to clean it
    df = pu.clean_order_data(df)
    # task 2 As the “Size” data in the 1st parameter table can be numeric and text values mixed,
    # convert “Size” column to STRING data type (otherwise only the texts will be matched, e.g. “XL”).
    paramlist_filt[1]['Size'] = paramlist_filt[1]['Size'].astype(str)
#    ic(paramlist_filt[1]['Size'])
    df['Size'] = df['Size'].astype(str)
#    ic( df['Size'])

    # task 3.d Filter it on only the rows with the Sizes and Countries specified for the input file
    # Special thanks to Szabolcs for suggesting a more general solution.
    filter_column_list = ['Size', 'Country']
    for i in range( len(paramlist_filt) ):
        for filter_column in filter_column_list:
            if filter_column in paramlist[i].columns:
                # filter column to values which are among the values in the appropriated column of the paramlist
                df = df[ df[filter_column].isin(paramlist_filt[i][filter_column].tolist()) ]

    # task 3.e Look upthe related Class Names of the class id’s (“H”, “M”, “L”), into a separate “Class Name” column
    df = pd.merge(df, paramlist[3], left_on= 'Class', right_on= 'Class ID', how= 'inner')

    # task 3.f Remove “Class” column, as we only need “Class ID” column instead
    df = df.drop(['Class'], axis = 1)

    # task 3.g translate headers based on the dictionary created from the lists coming from the columns of the parameter file
    df.columns = pd.Series(df.columns).replace(dict(zip(paramlist_filt[4]['Old header'].tolist(), paramlist_filt[4]['New header'].tolist())))
    # ic(df)

    # task 3.h and 3.i The output folder should be a “2011” / “2012” / “2013” / “2014” subfolder inside the “Output” folder
    # (based on input file’s name), the program should create these folders (if they do not exist) Use your “Export_to_csv.ipynb”
    # external program to export the cleaned, filtered, translated dataframe to the output folder, the output file’s name should be
    # the same as the input file, but with a “_cleaned_filtered_translated.csv” ending
    pu.export_to_csv(basepath, outputfolder + '\\' + inputfolder[-4 : ], inputfile[ : -4] + '_cleaned_filtered_translated.csv', df)

# task 6 At the end, write out the runtime, and a beep sound and a final printed message should notify the user.
endtime = time.time()
print(pu.calc_runtime(starttime, endtime))

# beep and final message
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)
print('All tasks are finished in week 5 Homework 5.')