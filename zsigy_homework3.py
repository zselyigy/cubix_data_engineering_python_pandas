# Homework 3 - Week 3
# Created by István Gy. Zsély
# version 0.1
# For details look in the README.md file.

# import the pandas data analysis library
import winsound, time


# define a function for the calculation of runtime in a string with a specific format
def runtime(start, end):
    hour, remainder = divmod(end - start, 3600)
    minute, second = divmod(remainder, 60)
    return 'Runtime {:0>2}:{:0>2}:{:05.2f}'.format(int(hour), int(minute), second)

# store the starttime
starttime = time.time()

# Tasks 1 to 3
# Read an integer number between 1 and 30
valid = False
while not valid:    # continously asks for input until all three conditions fulfilled
    n = input('Type an integernumber between 1 and 30: ')   # Task 1
    try:
        n_numeric = float(n)    # Task 2.a check if it a number or not
        int_number = int(n_numeric)
        if int_number == n_numeric:    # Task 2.b check if it is an integer
            if (int_number < 1) or (int_number > 30):    # Task 2.c check if its in the given range interpreting the interval as [1, 30]
                print('Number must be BETWEEN 1 and 30!')
            else:
                valid = True
        else:
            print('Number must be INTEGER!')    
    except:
        print('Type a NUMBER, not a text!')

# Task 4 Custom function for testing the divisibility of a number by a divisor
def is_divisible(number, divisor):
    if number % divisor == 0:
        d = True
    else:
        d = False
    return d

# Task 5
list_of_even_numbers = []
list_of_divisible_by_three = []
for i in range(1, int_number + 1):
    if is_divisible(i, 2):
        list_of_even_numbers.append(i)    # append the even number to the appropriate list
    if is_divisible(i, 3):
        list_of_divisible_by_three.append(i)    # append the number divisible by 3 to the approriate list

# Task 5.a
# print all even numbers or None if there is no such a number
if len(list_of_even_numbers) == 0:
    my_string = 'None'
else:
    my_string = str(list_of_even_numbers)[1: -1]
print('Even numbers in the interval of 1 and ' + str(int_number) + ': ' + my_string)
# Task 5.b
# print all numbers divisible by 3 or None if there is no such a number
if len(list_of_divisible_by_three) == 0:
    my_string = 'None'
else:
    my_string = str(list_of_divisible_by_three)[1: -1]
print('Divisible by 3 in the interval of 1 and ' + str(int_number) + ': ' + my_string)

# store the endtime and print runtime
endtime = time.time()
print(runtime(starttime, endtime))

# beep and final message
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)
print('All tasks are finished in week 3 Homework 3.')