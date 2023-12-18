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
basepath = r'.\Python_DA'
outputfolder = 'Output'

# task 1 Read the parameter tables from “Parameters_Homework4.xlsx”
# parameter related data
paramfolderpath = r'.\Python_DA\Homework4'
paramfile = 'Parameters_Homework4.xlsx'
paramfile_sheet = 'Parameter tables'
usedcolumnlist = ['A', 'C', 'E:F']
paramlist = []

# read the parameter file
paramlist = pu.read_parameters(paramfolderpath, paramfile, paramfile_sheet, usedcolumnlist)
print(paramlist)


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