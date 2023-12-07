text = 'Jack Bauer'
# from start until the first space
print(text[ : text.find(' ')])
# from the fist space to the end
print(text[text.find(' ') + 1 : ])

# define a function: reverse the first and second words (the two substrings, before and after the first space really)
def reversed_name(text):
    return text[text.find(' ') + 1 : ] + ' ' + text[ : text.find(' ')]

print(reversed_name(text))