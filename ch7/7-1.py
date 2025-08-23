'''
7-1. Rental Car:
Write a program that asks the user what kind of rental car they would like.
Print a message about that car, such as "Let me see if I can find you a Subaru."
'''
# what kind of rental car the user would like
prompt = input("What brand would you like to rent? ")
brand = prompt.upper()

print(f"\nLet me see if I can find you a {brand}.")