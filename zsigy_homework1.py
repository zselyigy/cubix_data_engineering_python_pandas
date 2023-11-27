# Homework 1 - Week 1
# Created by István Gy. Zsély

# Tasks:
# 1.Assign this text to a variable
mytext = 'Python is a high-level, general-purpose     programming language. Its design philosophy emphasizes code readability. \
Guido van Rossum, a Dutch       computer programmer, began working on    Python     in the late 1980s as a successor to the ABC \
programming language, and first released      it as Python 0.9.0 in 1991. Python 2.0 was released in 2000, and Python 3.0,\
released in 2008, was a major revision not completely    backward-compatible     with earlier versions. Python consistently\
ranks as one of the       most popular programming languages.The developers of Python     aim for it to be fun to use.\
 This is reflected in its name, a tribute to the      British comedy group Monty Python, and in occasionally playful approaches \
to tutorials       and reference materials.'

# 2.Break the text into multiple program lines in the cell, so that we don’t need to scroll the cell.
# This is not applicable in VS Code IDE, but I did it similar way in task 1.

# 3.Remove all the unnecessary spaces from the text (full trim).
mytext_unnecessary_spaces_removed = ' '.join(mytext.split());

# 4.Replace all “Python” words to upper case.
mytext_Python_uppercased = mytext_unnecessary_spaces_removed.replace('Python', 'PYTHON')

# 5.Within version numbers, change points (.) to underscores (_).
# Sorry, its a manual solution. The version number is not mentioned here as v*, but can be found in general by finding the following pattern: all of them contain "integer.integer" part.
mytext_version_numbers_underscored = mytext_Python_uppercased.replace('0.9.0', '0_9_0')
mytext_version_numbers_underscored = mytext_version_numbers_underscored.replace('2.0', '2_0')
mytext_version_numbers_underscored = mytext_version_numbers_underscored.replace('3.0', '3_0')

# 6.Insert line breaks after the end of each sentence.
mytext_linebreaks = mytext_version_numbers_underscored.replace('. ', '.\n')   # This way the . to _ transformation can be avoided.

# 7.Write out the cleaned text by print().
print('The cleaned text:\n'+mytext_linebreaks)

# 8.Find the position of the very first release of Python in the text, then use the slicing to write out only that part of the text which contains the name of the first release version and the year.
first_PYHTON_index = mytext_linebreaks.find('first release')
first_part = mytext_linebreaks[ : first_PYHTON_index]
revesed_first_part = first_part[ : : -1]
sentence_end_index_before = len(first_part) - revesed_first_part.find('\n.')
sentence_end_index_after = first_PYHTON_index + mytext_linebreaks[first_PYHTON_index : ].find('.\n')
sentence_of_the_information = mytext_linebreaks[sentence_end_index_before : sentence_end_index_after+1]
# Note: The case is not handled if the information is in the first or in the last sentence. This may lead to incorrect indexing.

# 9.Print a final message to the user.
print('\nThe text provides information about the year of the first release in this sentence: "{}"'.format(sentence_of_the_information))

# PS: Thanks for the interesting task!