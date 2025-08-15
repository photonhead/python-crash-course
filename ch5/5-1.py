'''
5-1. Conditional Tests: Write a series of conditional tests.
Print a stateent describing each test and your prediction for the results of each test.
Your code should look something like this:
------------------------------------------------------------
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
------------------------------------------------------------
1) Look closely at your results, and make sure you understand why each line evaluates to True or False.
2) Creat at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
'''

# grocery shopping list
grocery_shopping_list = ['milk', 'egg', 'bread', 'strawberries', 'blueberries', 'meat', 'fish', 'snacks', 'ice cream', 'potatoes', 'tomatoes', 'green onions', 'cup noodles', 'chicken wings', 'bbq sauce', 'japchae sauce', 'green beans']

# True
print("Does the grocery_shopping_list have 'blueberries'? I predict True.")
print('blueberries' in grocery_shopping_list)

print("Does the grocery_shopping_list have 'strawberries'? I predict True.")
print('strawberries' in grocery_shopping_list)

print("Does the grocery_shopping_list have 'potatoes'? I predict True.")
print('potatoes' in grocery_shopping_list)

print("Does the grocery_shopping_list have 'ice cream'? I predict True.")
print('ice cream' in grocery_shopping_list)

print("Does the grocery_shopping_list have 'fish'? I predict True.")
print('fish' in grocery_shopping_list)

# False
print("Does the grocery_shopping_list have 'broccoli'? I predict False.")
print('broccoli' in grocery_shopping_list)

print("Does the grocery_shopping_list have 'apple'? I predict False.")
print('apple' in grocery_shopping_list)

print("Does the grocery_shopping_list have 'apple'? I predict False.")
print('grapes' in grocery_shopping_list)

print("Does the grocery_shopping_list have 'apple'? I predict False.")
print('avocado' in grocery_shopping_list)

print("Does the grocery_shopping_list have 'apple'? I predict False.")
print('shrimp' in grocery_shopping_list)