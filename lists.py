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
