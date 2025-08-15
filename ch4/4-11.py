'''
4-11. My Pizzas, Your Pizzas: Start with your program from Ex4-1. 
Make a copy of the list of pizzas, and call it friend_pizzas.
Then do the following:
    1) Add a new pizza to the original list.
    2) Add a different pizza to the list friend_pizzas.
    3) Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend's favorite pizzas are:, and then use a for loop to print the second list.
    Make sure each new pizza is stored in the appropriate list.
'''
# copy the original list
pizzas = ['combination', 'hawaiian', 'creamy garlic', 'margherita']
friend_pizzas = pizzas[:]

# add a new, different pizza to each list
pizzas.append('savory anchovy')
friend_pizzas.append('chicken BBQ')

# print each list with messages
print(f"My favorite pizzas are:")
for myFav in pizzas:
    print(myFav.title())

print(f"\nMy friend's favorite pizzas are:")
for bfFav in friend_pizzas:
    print(bfFav.title())