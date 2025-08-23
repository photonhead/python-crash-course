'''
7-2. Restaurant Seating: 
Write a program that asks the user how many people are in their dinner group.
If the answer is more than eight, print a message saying they'll have to wait for a table.
Otherwise, report that their table is ready.
'''
# asks the user how many people in their dinner group
attendee_num = int(input("How many people for your dinner table? "))

if attendee_num > 8:
    print("I'm sorry but we're completely full right now for a large group. I can put you on our waiting list and text you when a table is ready.")
else:
    print("We have a table ready for you. Right this way, please!")