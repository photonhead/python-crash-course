glossary = {
    'variable': 'A variable is a named container that holds a value in a program.', 
    'string': 'A string is a sequence of characters, used to represent text in a program.', 
    'float': 'A float, or floating-point number, is a number that contains a decimal point.', 
    'integer': 'An integer is a whole number (positive, negative, or zero) with no fractional part.', 
    'list': 'A list is a data structure in Python that is an ordered and changeable collection of items.', 
    }

# add five new terms with definitions.
glossary['loop'] = 'A loop is a block of code that repeats.'
glossary['dictionary'] = 'A dictionary is a collection of key-value pairs.'
glossary['tuple'] = 'A tuple is an ordered, immutable collection of items'
glossary['boolean'] = 'A boolean is a data type that represents one of two values: True or False.'
glossary['comment'] = 'A comment is a note in a program that the Python interpreter ignores.'

# loop through the dictionary and print each term and its definition.
for term, definition in glossary.items(): 
    print(f"- {term.title()}: {glossary[term]}")