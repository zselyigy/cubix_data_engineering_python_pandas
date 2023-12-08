# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Input'
outputfolder = 'Output\\All periods'
outputfile = 'Revenues_all_periods.csv'

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

for inputfile in os.listdir(basepath + '\\' + inputfolder):
    exec(compile(source=open('Read_csv.py').read(), filename='Read_csv.py', mode='exec'))
    exec(compile(source=open('week2_Clean_data2.py').read(), filename='week2_Clean_data2.py', mode='exec'))
    exec(compile(source=open('Write_csv.py').read(), filename='Write_csv.py', mode='exec'))


# beep
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)

# store the endtime
endtime = time.time()
# print runtime
print(runtime(starttime, endtime))

print('All source files cleaned!')