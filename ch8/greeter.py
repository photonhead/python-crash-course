'''
def greet_user(username): # username -> parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

username = input("What's your name?: ") # username -> variable
greet_user(username) # username -> argument
'''
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# this is an infinite loop!
# put break points using if statements
while True:
    print("\nPlease tell me your name.")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")