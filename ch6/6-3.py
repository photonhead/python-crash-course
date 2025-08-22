'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let's call it a glossary.
- Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
- Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blankline between each word-meaning pair in your output.
'''
terms = ['variable', 'string', 'float', 'integer', 'list']

glossary = {
    'variable': 'A variable is a named container that holds a value in a program.', 
    'string': 'A string is a sequence of characters, used to represent text in a program.', 
    'float': 'A float, or floating-point number, is a number that contains a decimal point.', 
    'integer': 'An integer is a whole number (positive, negative, or zero) with no fractional part.', 
    'list': 'A list is a data structure in Python that is an ordered and changeable collection of items.'
    }

# get a term and find it in glossary, and then get its value.
for term in terms: 
    print(f"{term.title()}: {glossary[term]}")