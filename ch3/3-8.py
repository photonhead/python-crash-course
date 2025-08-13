'''
3-8. Seeing the World: Think of at least five places in the world you'd like to visit.
'''
# store the locations in a list. make sure the list is not in alphabetical order.
cities = ['new york', 'boston', 'washington', 'houston', 'new orleans']

# print your list in its original order.
print(f"1. Original list: {cities}")

# use sorted() to print your list in alphabetical order without modifying the actual list.
print(f"2. In alphabetical order: {sorted(cities)}")

# show your list is still in its original order by printing it
print(f"3. Original list again: {cities}")

# use sorted() to print your list in reverse-alphbetical order without changing the order of the original list
print(f"4. In reverse-alphabetical order: {sorted(cities, reverse=True)}")

# show that your list is still in its original order by printing it again.
print(f"5. Original list still same: {cities}")

# use reverse() to change the order of your list. Print the list to show that its order has changed.
cities.reverse()
print(f"6. Reversed my original list: {cities}")

# use reverse() to change the order of your list again. Print the list to show it's back to its original order.
cities.reverse()
print(f"7. Back to my original list: {cities}")

# use sort() to change your list so it's stored inalphabetical order. Print the list to show that its order has been changed.
cities.sort()
print(f"8. Sorted in alphabetical order permanently: {cities}")

# use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has been changed.
cities.sort(reverse=True)
print(f"9. Sorted in reverse-alphabetical order permanently: {cities}")