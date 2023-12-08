# Homework 3 - Week 3
# Created by István Gy. Zsély
# version 0.1
# For details look in the README.md file.

# import the pandas data analysis library
import pandas as pd, winsound, time


# define a function sor the calculation of runtime in a string with a specific format
def runtime(start, end):
    hour, remainder = divmod(end - start, 3600)
    minute, second = divmod(remainder, 60)
    return 'Runtime {:0>2}:{:0>2}:{:05.2f}'.format(int(hour), int(minute), second)

# store the starttime
starttime = time.time()

# Tasks 1 and 2
# read a number
valid = False
while not valid:
    n = input('Type an integernumber between 1 and 30: ')   # it provides a string all the time
    try:
        n_numeric = float(n)    # task 2.a check if it a number or not
        int_number = int(n_numeric)
        if int_number == n_numeric:    # task 2.b check if it is an integer
            if (n_numeric < 1) or (n_numeric > 30):    # task 2.c check if its in the given range interpreting the interval as [1, 30]
                print('Number must be BETWEEN 1 and 30!')
            else:
                valid = True
        else:
            print('Number must be INTEGER!')    
    except:
        print('Type a NUMBER, not a text!')

print('The number: ', int_number)


# Task 12
# final message to the user


# store the endtime
endtime = time.time()
# print runtime
print(runtime(starttime, endtime))

# beep and final message
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)
print('All tasks are finished in week 3 Homework 3.')