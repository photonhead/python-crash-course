'''
7-4. Pizza Toppings:
Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value.
As they enter each topping, print a message saying you'll add that topping to their pizza.
'''
prompt = "Please enter your desired topping one at a time."
prompt += "\n(Enter 'quit' when you're done.)"

desired_toppings = [] # topping container

while True:
    topping_order = input(prompt) # get user input
    
    if topping_order != 'quit': # as far as user didn't type 'quit'
        desired_toppings.append(topping_order) # get those input and add it to the list
        print(f"I'll add {desired_toppings} to your pizza.") # and let them know I added those toppings to their order
    else: # when they enter 'quit'
        break # stop and get out of this while loop

print(f"I'll add {desired_toppings} to your pizza. Thank you for your order!")