'''
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
- Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
- Use a loop to print the name of each river included in the dictionary.
- Use a loop to print the name of each country included in the dictionary.
'''
# make a dictionary
major_rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'yangtze': 'china'
}

# print a sentence about each river and its country
print("Fun Facts:")
for river, country in major_rivers.items():
    print(f"-The {river.title()} river runs through {country.title()}.")

# print the name of each river
print("Rivers in Dictionary:")
for river in major_rivers.keys():
    print(f"-{river.title()}")

# print the name of each country
print("Countries in Dictionary:")
for country in major_rivers.values():
    print(f"-{country.title()}")