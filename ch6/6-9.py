'''
6-9. Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
Loop through the dictionary, and print each person's name and their favorite places.
'''
# Make a dictionary called favorite_places. 
favorite_places = {
    'jay': 'nature',
    'jason': 'home',
    'sarah': 'Japan'
}

for name, place in favorite_places.items():
    print(f"{name.title()} likes {place}.")