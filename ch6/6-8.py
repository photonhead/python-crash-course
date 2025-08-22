'''
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner's name.
Store these dictionaries in a list called pets.
Next, loop through your list and as you do, print everything you know about each pet.
'''
# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner's name.
pet_0 = {
    'name': 'chacha',
    'category': 'dog',
    'owner': 'jay'
}

pet_1 = {
    'name': 'khai',
    'category': 'dog',
    'owner': 'jason'
}

pet_2 = {
    'name': 'beamo',
    'category': 'dog',
    'owner': 'sarah'    
}

pet_3 = {
    'name': 'freya',
    'category': 'cat',
    'owner': 'alex'    
}

pet_4 = {
    'name': 'mochi',
    'category': 'cat',
    'owner': 'cesar'    
}

pet_5 = {
    'name': 'bear',
    'category': 'dog',
    'owner': 'aaron'    
}

# Store these dictionaries in a list called pets.
pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

# loop through your list and as you do, print everything you know about each pet.
for pet in pets:
    print(pet)

# additional prints
for pet in pets:
    for items, details in pet.items():
        print(f"{items.title()}: {details.title()}")