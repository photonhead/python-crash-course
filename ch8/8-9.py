'''
8-9. Messages: Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.
'''
# make a list
messages = [
    'Good morning',
    'Good afternoon',
    'Good evening',
    'Good night'
]

# get a name from the user
name = input("what is your name? ")

# define a function to print each text msg
def show_messages(name, msg):
    for msg in messages:
        print(f"{msg}, {name.title()}!")

# call a function
show_messages(name, messages)