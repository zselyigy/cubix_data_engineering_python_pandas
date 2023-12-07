text = 'Jack Bauer'
# from start until the first space
print(text[ : text.find(' ')])
# from the fist space to the end
print(text[text.find(' ') + 1 : ])

# define a function: reverse the first and second words (the two substrings, before and after the first space really)
def reversed_name(text):
    return text[text.find(' ') + 1 : ] + ' ' + text[ : text.find(' ')]

print(reversed_name(text))

import time
# define a function sor the calculation of runtime in a string with a specific format
def runtime(start, end):
    hour, remainder = divmod(end - start, 3600)
    minute, second = divmod(remainder, 60)
    return 'Runtime {:0>2}:{:0>2}:{:05.2f}'.format(int(hour), int(minute), second)

# store the starttime
starttime = time.time()

import winsound   # this is the module of windows sounds
# beep
frequency = 440  # in Hz
duration = 500  # in ms
winsound.Beep(frequency, duration)

# store the endtime
endtime = time.time()
# print runtime
print(runtime(starttime, endtime))