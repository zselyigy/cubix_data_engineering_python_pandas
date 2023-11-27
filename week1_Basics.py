# this is a comment
# we add 2 numbers
a = 5
b = 3
print(a + b)

a = 'Text1'
b = "Text2"
print(a + b)

# use lower case for your variables, do not use space, but underline
full_name = 'Jack'
# this is camel case
fullName = 'Jack'

a = 6
b = 'Jack'
print(a, b)


basepath = r'.\\Python_DA'
print(basepath)

# import the os module to access the operating system related functions
import os
# the file list of the Python_DA folder
print(os.listdir(basepath))
# the file list of the Python_DA\input folder
print(os.listdir(basepath + '\\input'))

# get the current working directory
current_workingdir = os.getcwd()
print(current_workingdir)

