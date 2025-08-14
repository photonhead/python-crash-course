# Store the names of your favorite pizza in a list
pizzas = ['combination', 'hawaiian', 'creamy garlic', 'margherita']
'''
# use a for loop to print the name of each pizza
for pizza in pizzas:
    print(pizza)

# modify your for loop to print a sentence using the name of the pizza, instead of printing joust the name of the pizza.
for pizza in pizzas:
    print(f"I love {pizza.title()} pizza!")
'''
# add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
for pizza in pizzas:
    print(f"I love {pizza.title()} pizza!")
print(f"\nI love them all, but my best pick is {pizzas[-1].title()} pizza.\nJuicy tomato and fresh basil are just perfect combo with mozzarella cheese!\nI really love it!")