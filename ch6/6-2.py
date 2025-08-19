'''
6-2. Favorite Numbers: Use a dictionary to store people's favorite numbers.
Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary.
Print each person's name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.
'''
names = ['sarah', 'jay', 'jason', 'alex']

favorite_numbers = {
    'sarah': 3,
    'jay': 1,
    'jason': 7,
    'alex': 9
}

for name in names:
    if name == favorite_numbers['sarah']:
        print(f"{name.title()}'s favorite number is {favorite_numbers['sarah']}.")
    elif name == favorite_numbers['jay']:
        print(f"{name.title()}'s favorite number is {favorite_numbers['jay']}.")
    elif name == favorite_numbers['jason']:
        print(f"{name.title()}'s favorite number is {favorite_numbers['jason']}.")
    else:
        print(f"{name.title()}'s favorite number is {favorite_numbers['alex']}.") 