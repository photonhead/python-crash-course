'''
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as 'I made your tuna sandwich.'
As each sandwich is made, move it to the list of finished_sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made.
'''
# make a list and fill it with various sandwiches.
sandwich_orders = ['blt', 'tuna', 'ham & egg', 'pb & j']
sandwich_orders.reverse()

# # test: the reversed list?
# print(f"Sandwich Orders (reverse order): {sandwich_orders}")

# make an empty list called finished_sandwiches.
finished_sandwiches = []

#loop through the list of sandwich orders and print a msg for each order.
while sandwich_orders:
    ordered = sandwich_orders.pop()

    print(f"I made your {ordered.upper()} sandwich.")
    finished_sandwiches.append(ordered)

# display all the sandwiches have been made
print("--- Ordered Sandwiches ---")
for sandwich in finished_sandwiches:
    print(sandwich.upper())

# # test: appending order == original order?
# print(f"\nFinished sandwiches: {finished_sandwiches}") 