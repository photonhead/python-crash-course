'''
6-11. Cities: Mkae a dictionary called cities.
Use the names of three cities as keys in your dictionary.
Creat a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.
The keys for each city's dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.
'''
# make a dictionary called cities.
# use the names of three cities as keys in your dictionary.
# information about each city's country, population, and one fact about that city.
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
    }
}

# Print the name of each city and all of the information you have stored about it.
for city, details in cities.items():   
    item_0 = details['country']
    item_1 = details['population']
    item_2 = details['fact']

    print(f"{city.upper()}:")
    print(f"-Country: {item_0.title()}")
    print(f"-Population: {item_1} residents (2024)")
    print(f"-Fun Fact: {item_2.title()}\n")