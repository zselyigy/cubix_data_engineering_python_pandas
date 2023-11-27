a = 'Jack Bauer Jack fasdf'
# convert a string to upper case
print(a.upper())
# convert a string to lower case
print(a.lower())



b = 'jack Bauer'
# convert a string to title case
print(b.title())

b = ' \t aa    bb \f   '
print(b)
# removes any leading, and trailing whitespaces 
c = b.strip()
print()

# replace a part of the strig with a new one, does it for each occurence
a = a.replace('Jack', 'John')
print(a)

# replace double spcaes to single ones
print(c.replace('  ', ' '))

s = 'Anaconda'
# starting position of a substring from the left, in case of multiple occurence only the first index appears
print(s.find('Ana'))
print(s.find('ana'))  # in case of it doesn't contain this results -1
print(s.find('con'))

# check whether the string starts with a substring
a = 'Jack Bauer'
print(a.startswith('Jack'))
print(a.startswith('jack'))
print(a.endswith('Jack'))

print(s[3])         # index starts from 0
print(s[ : 4])      # the endpoint is not included
print(s[3 : ])      # the starting point included
print(s[-3 : ])     # negative numbers count from the end
print(s[3 : 6])
print(s[3 : 9 : 2]) # third parameter is the stepping
print(s[ : : -1])   # reverses the string
print(s[ : : -3])   # reverse and only every third character
sz = '12345678'
print(sz[6 : : -2])   # reverse from index 6 and only every second character
print(sz[7 : : -2])   # reverse from index 7 and only every second character
print(sz[8 : : -2])   # reverse from index 8 and only every second character (bigger than len doesn't have any effect)
print(sz[9 : : -2])   # reverse from index 9 and only every second character (bigger than len doesn't have any effect)

substring = 'language'
mainstring = "Python is a cool programming language, isn't it?"
substring_start = mainstring.find(substring)
substring_length = len(substring)
print(substring_length)
substring_end = substring_length + substring_start
print(substring_start, substring_end)

# part of string between two positions
sliced_part = mainstring[substring_start : substring_end]
print(sliced_part)
print(sz[10 : 5 : -1], len(sz[10 : 5 : -1]))