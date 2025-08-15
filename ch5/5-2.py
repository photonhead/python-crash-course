'''
5-2. More Conditional Tests: You don't have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
    # Tests for equlity and inequlity with strings
    # Tests using the lower() method
    # Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.
    # Tests using the 'and' keyword and the 'or' keyword.
    # Test whether an item is in a list
    # Test whether an item is not in a list
'''
# Tests for equlity and inequlity with strings
car = 'audi'
print("Is car 'audi'? I predict True.")
print(car == 'audi')

print("Is car 'bmw'? I predict False.")
print(car == 'bmw')

# Tests using the lower() method
car = 'BMW'
car.lower() == 'bmw' # True

car = 'AUDI'
car.lower() == 'bmw' # False

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.
numbers = [25, 35, 45, 55]

for num in numbers:
    if num < 40:
        print(num, "is less than 40.") # 25, 35
    else:
        print(num, "is greater than 40.") # 45, 55

for num in numbers:
    if num == 45:
        print("num == 45 is", num == 45, f"This num is {num}.") # True
    else:
        print("num == 45 is", num == 45, f"This num is {num}.") # False

for num in numbers:
    if num > 40:
        print(f"{num} is great than 40.") # 45, 55
    else:
        print(f"{num} is less than or equal to 40.") # 25, 35 

# Tests using the 'and' keyword and the 'or' keyword.
# Test whether an item is in a list
# Test whether an item is not in a list
groceries = ['milk', 'egg', 'bread', 'fish', 'fruits', 'vegetables', 'meat']

for food in groceries:
    if food == 'milk':
        print("Milk is in the grocery shopping list.")
    else:
        print(f"{food} is not milk.")

for food in groceries:
    if food != 'fruits':
        print(f"{food} is in the list, but it's not fruits.")
    else:
        print(f"Are {food} in the list?", food == 'fruits') # True
        
for food in groceries:
    if food != 'egg' and food != 'bread':
        print("Egg or bread is missing!")
    else: 
        exit()

for food in groceries:
    if food == 'meat' or food == 'fish':
        print("We have at least one protein")
    else:
        exit()