'''
5-7. Favorite Fruit:
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
- Make a list of your three favorite fruits and call it favorite_fruits.
- Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!
'''

# make a list of my favorite fruits
favorite_fruits = ['strawberry', 'blueberry', 'rapsberry']
'''
# write five independent if statements that check for certian fruits in my list, and print a statement
if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")
if 'blueberry' in favorite_fruits:
    print("You really like blueberries!")
if 'rapsberry' in favorite_fruits:
    print("You really like rapsberries!")
if 'peach' in favorite_fruits:
    print("You really like peaches!")
if 'passion fruit' in favorite_fruits:
    print("You really like passion fruits!")
'''

fruit = input("What is your favorite fruit?")

if fruit in favorite_fruits:
    print(f"We have {fruit}. You really like {fruit}!")
else:
    print(f"Uh-oh, {fruit} is not in our list. Sorry!")
    request = input("Do you want to add it to our list? Please type 'y' for addition, and 'n' for 'never mind.'")
    if request == 'y':
        favorite_fruits.append(fruit)
        print(f"Now we have {fruit} in our list! Here is our selection: {favorite_fruits}")
    else:
        print(f"Ok! No worries! Here is our selection for your reference: {favorite_fruits}")