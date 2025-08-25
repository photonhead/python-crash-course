'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True # variable 'active' set 'True'
while active: 
    message = input(prompt) # while active is as-is, get msg from the user

    if message == 'quit': # if msg is 'quit', active changes to 'False'
        active = False
    else: # if msg is not 'quit', print msg
        print(message)