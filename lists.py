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

# concatenate elements of list
names = ['Jack', 'Jill', 'Robert', 'Susan']
print('-'.join(names))

# remove all extra spaces from the text (full trim)
a = '    asa    b      '
print(' '.join(a.split()))

# remove the non-numeric items from the list
import pandas as pd
itemlist = [1, 2, 'Jack', 4]
new_itemlist = list(pd.to_numeric(itemlist, errors= 'coerce'))
print(new_itemlist)
# if the item is not equal to itself it is NaN
print(new_itemlist[1] == new_itemlist[1], new_itemlist[2] == new_itemlist[2])
# remove the NaN items from the list
itemlist = [x for x in new_itemlist if x == x]
print(itemlist)

# find difference between lists
def listdiff(list1, list2):
    return [i for i in list1 + list2 if (i not in list1) or (i not in list2)]

names1 = ['Jack', 'Jill', 'Robert', 'Susan']
names2 = ['Joan', 'Roberto', 'Jack', 'Susan']
print(listdiff(names1, names2))

# delete variables
print(names1)
del names1
# print(names1)

# a pecific element of a list can be deleted
del names2[2]
print(names2)