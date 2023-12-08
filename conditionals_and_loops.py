a = 5
# if a is EQUAL to 5
if a == 5:
    print('True')
else:
    print('False')

# if a is GREATER THAN 5
if a > 5:
    print('True')
else:
    print('False')

# if a is NOT EQUAL to 5
if a != 5:
    print('True')
else:
    print('False')

a = 6
# if a even
if a % 2 == 0:
    print('Can be divided by 2')
elif a % 3 == 0:   # if a cam be divided by 3
    print('Cannot be divided by 2, but can be divided by 3')
else:
    print('Cannot be divided by either 2 or 3')


# do it in one line (shorthand) in case only one line is for both cases
a = 6
b = 8
print('They are equal') if a == b else print('They are NOT equal')


# application of IF in conjuction with a text search
# print a message if the text contains a substring
a = 'Jack Bauer'
if a.find('Jfack') >=0:
    print('Contains.')
else:
    print('Does not contain.')

# a simpler way:
if 'Jack' in a:
    print('Contains.')
else:
    print('Does not contain.')

# make it case insensitive
if 'jack' in a.lower():
    print('Contains.')
else:
    print('Does not contain.')

# if the text starts with a substring:
if a.startswith('Jack'):
    print('Starts with it.')
else:
    print('Does not start with it.')

# if the text ends with a substring:
if a.endswith('Jack'):
    print('Ends with it.')
else:
    print('Does not end with it.')

v = True
if v:
    print('v is True.')
else:
    print('v is False.')

v = True
if not v:
    print('v is False.')
else:
    print('v is True.')

# the FOR loop
for i in range(5):   # range starts from 0 to the value before the number
    print(i)

print(' ')

# loop throught the even numbers from 4 to 10
for i in range(4, 11, 2):
    print(i)


# the WHILE loop
i = 1
# repeat the instruction while i <= 5
while i <= 5:
    if i % 2 == 0:
        print(str(i) + ' even')
    else:
        print(str(i) + ' odd')
    i += 1


# read a number
valid = False
while not valid:
    n = input('Type a number: ')   # it provides a string all the time
    try:
        n_numeric = float(n)
        valid = True
    except:
        print('Type a NUMBER, not a text!')

print('The number squared: ', n_numeric ** 2)
