'''
7-10. Dream Vacation:
Write a program that polls users about their dream vacation.
Write a prompt similar to 'if you could visit one place in the world, where would you go?'
Include a block of code that prints the results of the poll.
'''
# make an empty list for vacation locations
vacation_locations = []

# ask users where they want to go for a vacation
prompt = "If you could visit one place in the world, where would you go?"
prompt += "\n(When you want to stop, enter 'stop'): "

active = True

while active:
    response = input(prompt)

    if response != 'stop': 
        vacation_locations.append(response)
        continue
    else:   # when user type 'stop'
        active = False
        break

# print the results of poll
# if there's no location submitted, print a special msg
if len(vacation_locations) == 0:
    print("\nYou didn't submit your dream vacation location.") # special msg
else: 
    print(f"\nYour dream vacation: ") # list of dream vacation
    for vacation in vacation_locations:
        print(f"- {vacation.title()}")
    
    print("\nThank you for participating!")