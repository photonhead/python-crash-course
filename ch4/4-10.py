'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
    1) Print the message The first three items in the list are:. Then use a slice to print the first three items from that program's list.
    2) Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
    3) Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
'''

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
print(f"There are {len(colors)} colors in rainbow, and they are {colors}.")

# first three items
print(f"The first three colors are {colors[:3]}.")

# three items in the middle
print(f"Three colors in the middle of the rainbow are {colors[2:5]}.")

# last three items
print(f"The last three colors are {colors[-3:]}.")