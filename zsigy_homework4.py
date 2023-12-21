# Homework 4 - Week 4
# Created by István Gy. Zsély
# version 0.1
# For details look in the README.md file. (task 10)

# import modules
import pandas_utility_functions as pu       # module of the utility functions
import pandas as pd, os, winsound, time

# store the starttime
starttime = time.time()

# base path related variables
basepath = r'.\Python_DA\Homework4'
outputfolder = 'Output'
inputfolder = 'Input'

# task 1 Read the parameter tables from “Parameters_Homework4.xlsx”
# parameter related data
paramfolderpath = r'.\Python_DA\Homework4'
paramfile = 'Parameters_Homework4.xlsx'
paramfile_sheet = 'Parameter tables'
usedcolumnlist = ['A', 'C', 'E:F']
paramlist = []

# read the parameter file
paramlist = pu.read_parameters(paramfolderpath, paramfile, paramfile_sheet, usedcolumnlist)
#print(paramlist)

# task 2 Loop through the input files of the input folder, use your “Read_csv.ipynb” external program to read all of them, and append them into 1 dataframe.
# create an empty list for the series of dataframes read
df_list = []

# loop through all files in the inputfolder
for inputfile in os.listdir(basepath + '\\' + inputfolder):
    # read the file to df_one dataframe
    df_one = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8')
    # append it to the list of dataframes
    df_list.append(df_one)

# concatenate the dataframes
df = pd.concat(df_list)

# print progress message
print('Input files read.')

# task 4 Run this “Clean_order_data.ipynb” external program to clean the dataframe
# clean the dataframe using the code based on Week 2 Homework 2
df = pu.clean_order_data(df)

# task 5 As the “Size” data in the 1st parameter table can be numeric and text values mixed,
# convert “Size” column to STRING data type (otherwise only the texts will be matched, e.g. “XL”)
df['Size'] = df['Size'].astype(str)
paramlist[0]['Size'] = paramlist[0]['Size'].astype(str)

# task 6 Filter the dataframe on only the rows with the Sizes and Countriesin the parameter file
df = df[df['Size'].isin(paramlist[0]['Size'].tolist())]
print(paramlist[0]['Size'].tolist())



print(df)


# create the output folder
try:
    os.mkdir(basepath + '\\' + outputfolder)
except:
    pass




# store the endtime and print runtime
endtime = time.time()
print(pu.calc_runtime(starttime, endtime))

# beep and final message
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)
print('All tasks are finished in week 4 Homework 4.')