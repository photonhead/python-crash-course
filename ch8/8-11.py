'''
8-11. Archived Messages: Start with your work from Ex 8-10.
Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your lists to show that the original list has retained its messages.
'''
def send_messages(name, prepared_messages, sent_messages):
    print(f"\nThe following messages were prepared:")
    for prepared_message in prepared_messages:
        print(prepared_message)

    print("\n")

    while prepared_messages:
        current_msg = prepared_messages.pop()
        print(f"- {current_msg}, {name.title()}!")
        sent_messages.append(current_msg)

    print(f"\nThe following messages were sent:")
    for sent_message in sent_messages:
        print(sent_message)

prepared_messages = ['Good morning', 'Good afternoon', 'Good evening', 'Good night'] # text messages list
sent_messages = [] # empty list for sent messages

name = input("what is your name? ") # get a name from the user

# call a function
send_messages(name, prepared_messages[:], sent_messages)

# check the original list unchanged
print(prepared_messages) 
print(sent_messages) # reverse ordered (because of pop())