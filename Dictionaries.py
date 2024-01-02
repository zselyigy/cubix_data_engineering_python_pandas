# create a dictionary
english_to_german = {'Year': 'Jahr', 'Month': 'Monat', 'Data': 'Datum'}
personal_data = {'Name': 'Peter', 'Age': 36, 'Country': 'UK'}

# value for the key in the dictionary
print(personal_data['Age'])

# get all the keys of a dictonary
print(personal_data.keys())

# get all the values of a dictonary
print(personal_data.values())

# get all items (key - value pairs) of a dictonary
print(personal_data.items())

# modify a value for a key in a dictionary
personal_data['Age'] = 30
print(personal_data)

# loop through the items of dictionary
for i in personal_data:
    print(i, '-', personal_data[i])

# loop through the items of dictionary - an alternative way
for key, value in personal_data.items():
    print(key, '-', value)

# add a new item (key-value pair) to the dictionary
personal_data['Height'] = 180
print(personal_data)