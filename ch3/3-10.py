'''
3-10. Every Function: Think of things you could store in a list.
(ex: mountains, rivers, countires, cities, languages)
Write a program that creats a list containing these items and then uses each function introduced in this chapter at least once.
'''
# Countries I would like to visit someday in the future.
countries = ['iceland', 'netherlands', 'belgium', 'madagascar', 'nepal', 'switzerland', 'maldives', 'costa rica', 'brazil', 'india', 'malawi', 'tanzania', 'philippines', 'vietnam', 'malta', 'france', 'germany', 'monaco', 'sweden', 'cuba', 'morocco', 'turkey', 'new zealand', 'egypt', 'italy', 'united kingdom', 'kenya']

# print the original list
print(f"1. Original list: {countries}")

# sorted() in alphabetical order
print(f"2. Sorted in alphabetical order: {sorted(countries)}")

# sorted() in reverse-alphabetical order
print(f"3. Sorted in reverse-alphabetical order: {sorted(countries, reverse=True)}")

# show the original list
print(f"4. Original list again: {countries}")

# reverse() the list
countries.reverse()
print(f"5. Reverse the original list: {countries}")

# reverse() the list once again to return the list to its original order
countries.reverse()
print(f"6. Reverse the list again to return the list to its original status: {countries}")

# how many countries in the list? use len()
numCountries = len(countries)
print(f"7. How many countries in the list?: {numCountries} countries")

# sort the list in alphabetical order permanently
countries.sort()
print(f"8. Sorted in alphabetical order permanently: {countries}")

# sort the list in reverse-alphabetical order permanently
countries.sort(reverse=True)
print(f"9. Sorted in reverse-alphabetical order permanently: {countries}")