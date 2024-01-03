## inital section - base data, necessary modules and functions

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Input'
inputfile = 'Source.csv'
outputfolder = 'Output\\Filtered'
outputfile = 'Source_filtered.csv'


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


## main section - filter, clean files etc.

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