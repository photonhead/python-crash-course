'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that's being ordered.
Call the function three times, using a different number of arguments each time.
'''
# make a function to collect as many items as the function call provides and print a summary of the sandwich
def make_sandwich(*ingredients):
    print(ingredients) # wanna check each tuple

    print("\nThe following ingredients are being added:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# call the function three times with different number of arguments
make_sandwich('cheese') 
make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('ciabatta bread', 'sliced avocado', 'fried egg', 'baby kale')

# When tuple has one item only, the result shows a comma after the item because 
#  tuples are technically defined by the presence of a comma. (p.66)
# make_sandwich('cheese') --> printed to: ('cheese',) 