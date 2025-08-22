'''
6-12. Extensions: We're now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
'''
# use one of the programs and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.

# change 1 (extension): add two more cities and their information as key-value pairs to the dictionary
cities = {
    'seoul': {
        'country': 'south korea',
        'population': '9,605,419 (9.6 million)',
        'fact': 'Seoul is located only 35 miles from the border with North Korea, yet the air route between Seoul Gimpo (GMP) and Jeju Island is the busiest in the world.'
    },

    'seattle': {
        'country': 'united states',
        'population': '780,995 (0.8 million)',
        'fact': 'Despite its reputation, Seattle receives less annual rainfall than cities like New York.'        
    },

    'tokyo': {
        'country': 'japan',
        'population': '37,115,000 (37.1 million)',
        'fact': 'Tokyo\'s metropolitan area, which includes surrounding prefectures, is the world\'s largest, with over 37 million residents.'        
    },

    'london': {
        'country': 'united kingdom',
        'population': '9,748,000 (9.1 million)',
        'fact': 'London is technically considered a forest by the UN because of the density of trees per square mile.'        
    },

    'reykjavik': {
        'country': 'iceland',
        'population': '136,894 (0.1 million)',
        'fact': 'Reykjavík\'s tallest building is not an office tower, but the impressive Hallgrímskirkja church, which is 74.5 meters (244 feet).'        
    }
}

# change 2 (addition): first, print what cities in the dictionary as a list
city_names = []
for city_name in cities.keys():
    city_names.append(city_name)

# print(city_names) # city_names list test

# change 3: ask the user which city's information they are interested in
request_city = input("Which city do you want to know?").lower()

# test whether the city is in the list or not
if request_city not in city_names:
    print("There is no information about the city. You can look up these cities:")
    print(city_names)
    request_city = input("Which city do you want to know?").lower()    

# change 4: print city's name and its information wither improved formatting of the output 
if request_city in city_names:
    for city, details in cities.items():
        city_0 = cities['seoul']
        city_1 = cities['seattle']
        city_2 = cities['tokyo']
        city_3 = cities['london']
        city_4 = cities['reykjavik']
        
        item_0 = details['country']
        item_1 = details['population']
        item_2 = details['fact']

        if request_city == city:
            print(f"{city.upper()}:")
            print(f"\t-Country: {item_0.title()}")
            print(f"\t-Population: {item_1} (2024)")
            print(f"\t-Fun Fact: {item_2}\n")