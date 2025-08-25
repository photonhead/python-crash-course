'''
7-9. No Pastrami: 
Using the list sandwich_orders from Ex 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches.
'''
# add three 'pastrami' to the list 'sandwich_orders'
sandwich_orders = ['pastrami', 'blt', 'tuna', 'pastrami','ham & egg', 'pb & j', 'tuna', 'pastrami', 'ham & cheese']
print(f"- Your original order: {sandwich_orders}")

sold_out = 'pastrami'
finished_sandwiches = []

while sandwich_orders:
    # print a msg saying the deli has run out of pastrami
    print("\nUnfortunately, we are out of Pastrami at the moment.")

    # remove 'pastrami' from the list sandwich_orders
    while sold_out in sandwich_orders:
        sandwich_orders.remove(sold_out)
        continue

    # check there's no more 'pastrami' in the list
    if sold_out not in sandwich_orders:
        finished_sandwiches = sandwich_orders[:] # copy the order to finished_sandwiches list
        print(f"\n- Your revised order: {finished_sandwiches}")
        break

# counting how many sandwiches in each
num_pastrami = finished_sandwiches.count('pastrami')
num_blt = finished_sandwiches.count('blt')
num_tuna = finished_sandwiches.count('tuna')
num_ham_egg = finished_sandwiches.count('ham & egg')
num_pb_j = finished_sandwiches.count('pb & j')
num_ham_cheese = finished_sandwiches.count('ham & cheese')

# display all the sandwiches have been made
print("\n--- Ordered Sandwiches ---")
for sandwich in set(finished_sandwiches):
    if sandwich == 'pastrami':
        print(sandwich.title(), num_pastrami)
    elif sandwich == 'blt':
        print(sandwich.upper(), num_blt)
    elif sandwich == 'tuna':
        print(sandwich.title(), num_tuna)
    elif sandwich == 'ham & egg':
        print(sandwich.title(), num_ham_egg)
    elif sandwich == 'pb & j':
        print(sandwich.upper(), num_pb_j)
    elif sandwich == 'ham & cheese':
        print(sandwich.title(), num_ham_cheese)

confirm = input("\nConfirm? (yes/no): ")
if confirm == 'no':
    print("\nPlease call us to update your order!")
else:
    print("\nThank you for your order!")