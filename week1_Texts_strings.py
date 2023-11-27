a = 'Jack Bauer Jack'
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