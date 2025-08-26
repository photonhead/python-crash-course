'''
8-6. City Names:
Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this:

"Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are returned.
'''
# define a function
def city_country(city, country):
    city = f"{city.title()}"
    country = f"{country.title()}"
    formatted_city_country = f"\"{city}, {country}\""
    return print(formatted_city_country)

# call your function with at least three city-country pairs and print the values
city_country('seattle', 'united states')
city_country('seoul', 'south korea')
city_country('buenos aires', 'argentina')