'''
7-6. Three Exits:
Write different versions of either x 7-4 or 7-5 that do each of the following at least once:
- Use a conditional test in the while statement to stop the loop.
- Use an active variable to control how long the loop runs.
- Use a break statement to exit the loop when the user enters a 'quit' value.
'''
active = True 

while active:
    age = int(input("Ticket prices vary depending on age. What is your age?: "))
    if age < 3:
        print(f"The ticket is free!")
    elif age >= 3 and age < 12:
        print(f"The ticket price is $10.")
    else:
        print(f"The ticket price is $15.")

    prompt = input("Please enter 'quit' to stop. Do you want to stop?: ")
    if prompt != 'quit':
        continue
    else:
        break 

print("Thank you!")