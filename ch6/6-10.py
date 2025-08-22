'''
6-10. Favorite Numbers:
Modify your program from Ex 6-2, so each person can have more than one favorite number.
Then print each person's name along with their favorite numbers.
'''
# modify 6-2 program (each person can have more than one favorite number)
favorite_numbers = {
    'sarah': [3],
    'jay': [3, 7, 81, 19],
    'jason': [42],
    'alex': [9, 5]
}

# print each person's name along with their favorite numbers.
for name, number in favorite_numbers.items():
    if len(number) == 1:
        print(f"{name.title()}'s favorite number is {number}.")
    if len(number) > 1:
        print(f"{name.title()}'s favorite numbers are {number}.")