cars = ['bmw', 'audi', 'toyota', 'subaru']

# cars.sort() # in alphabetical order, permanently
# cars.sort(reverse=True) # reverse-alphabetical order, permanently 
'''
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

# The sorted() function can also accept a reverse=True argument if you want to display a list in reverse-alphabetical order.
print("\nHere is the reverse-sorted list: ")
print(sorted(cars, reverse=True))

print("\nStill your list remains same as original: ")
print(cars)
'''
'''
# print original list
print(cars)

cars.reverse() 
# permanently changed the list
# simply reverse the order of the list, doesn't sort backward alphabetically
# 리스트를 바꾸긴 하지만, 단순 역순으로 재정렬한 것이라 원래 리스트로 되돌리려면 한번 더 reverse()를 쓰면 쉽게 원래 리스트로 바꿀 수 있다.

print(cars)
'''

# finding the length of a list / the number of items in the list
numItems = len(cars)
print(numItems)