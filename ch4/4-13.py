# five basic foods in buffet, store those five simple foods in a tuple
buffet = ('gimbap', 'tteokbokki', 'ramyeon', 'gimmari', 'donggasu')

# use a for loop to print each food the restaurant offers
print("Our restaurant offers: ")
for food in buffet:
    print(food)

'''
# try to modify one of the items, and make sure that Python rejects the change
buffet[-1] = 'japchae'
print(buffet)
'''

# the restaurant changes its menu, replacing two of the items with different foods. 
# add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
buffet = ('gimbap', 'japchae', 'ramyeon', 'gimmari', 'udong')

print("\nOur restaurant revised our menu. Now we offer:")
for food in buffet:
    print(food)