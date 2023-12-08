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
elif a % 3 == 0:
    print('Cannot be divided by 2, but can be divided by 3')
else:
    print('Cannot be divided by either 2 or 3')


# do it in one line (shorthand) in case only one line is for both cases
a = 6
b = 8
print('They are equal') if a == b else print('They are NOT equal')

