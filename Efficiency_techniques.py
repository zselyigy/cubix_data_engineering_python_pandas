import datetime as dt

birth_date = dt.date(2020, 3, 21)
print(birth_date)
print(birth_date.strftime('%x'))    # local date
print(birth_date.strftime('%Y'))    # year full
print(birth_date.strftime('%m'))    # month number
print(birth_date.strftime('%B'))    # month full name
print(birth_date.strftime('%d'))    # day as number (1-31)
print(birth_date.strftime('%A'))    # day full name34
print(birth_date.strftime('%w'))    # weekday as a number (0-6), 0 is SUnday

today_date = dt.datetime.now()
print(today_date)
print(today_date.strftime('%x'))

a = 6
b = 0
try:
    print('The quotient is ' + str(a / b))
except:
    print('We cannot divide by zero!')

# n = input('Type a number: ')
n = 4
try:
    print('The number squared: ', float(n) ** 2)
except:
    print('Type a NUMBER, not a text!')

import os, shutil
basepath = r'.\Python_DA'
subfolder = 'Test folder'
# create a folder (if it does not exist)
try:
    os.mkdir(basepath + '\\' + subfolder)
except:
    pass   # in case of error (e.g. the subfolder exists) do nothing

# # remove a folder (only if empty)
# try:
#     os.rmdir(basepath + '\\' + subfolder)
# except:
#     pass   # in case of error (e.g. the subfolder is not empty) do nothing

# remove a folder with all files in
shutil.rmtree(basepath + '\\' + subfolder, ignore_errors = True)
