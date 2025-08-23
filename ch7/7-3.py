'''
7-3. Multiples of Ten:
Ask the user for a number, and then report whether the number is a multiple of 10 or not.
'''
# ask the user for a number
number = int(input("Choose any number you want to know whether the number is a multiple of 10 or not: "))

# report the result
if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nThe number {number} is NOT a multiple of 10.")