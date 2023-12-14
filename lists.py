names = ['Jack', 'Jill', 'Robert', 'Susan']

# length of lists (it counts the number of items
print(len(names))
print(names[0])

# add a new item to the end of the list
names.append('Peter')
print(names)

# names2 = ['dsad', 'dfasdfsa']
# names.append(names2)   # appending a list appends the whole list as a single element
# print(names)

# insert a new item to a specific position of the list
names.insert(1, 'Peter')
print(names)

# remove item from the list
names.remove('Jill')
print(names)

# remove all items from the list
names.clear()
print(names)

# concatenate lists
names1 = ['Jack', 'Jill', 'Robert', 'Susan']
names2 = ['Jack', 'Jill', 'Robert', 'Susan']
names3 = names1 + names2
print(names3)

# loosp through the elements of the list
names = ['Jack', 'Jill', 'Robert', 'Susan']
for name in names:
    print(name)

# loop through the elements of the list having the indexes during the process
names = ['Jack', 'Jill', 'Robert', 'Susan']
for i in range(len(names)):
    print(str(i) + ' ' + names[i])

# reach the elements by index
print(names[1])
print(names[-2])    # larger negative index than the length of the list causes IndexError

# check if something is an element of the list or not
a = 'Jill'
if a in names:
    print('It is in the list.')
else:
    print('It is not in the list.')

# splitting text to a list
a = '10/March/2020'
print(a.split('/'))

a = '    asa    b      '
print(a.split())   # having an empty call of .split it assumes WHITESPACESE and ignores the empty list elements / handles multiple WHITESPACES as ones

a = 'Jill SUsan Smith'
print(a.split()[0])