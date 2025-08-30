'''
8-10. Sending Messages: Start with a copy of your program from Ex 8-9.
Write a function called send_messages() that prints each text message 
and move each messages to a new list called sent_messages as it's printed.
After calling the function, print both of your lists to make sure the messages were moved correctly.
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
send_messages(name, prepared_messages, sent_messages)

# check whether the list items moved from prepared_messages to sent_messages successfully
print(prepared_messages) # original list -> should be empty
print(sent_messages) # reverse ordered (because of pop())