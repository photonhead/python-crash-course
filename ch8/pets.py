'''
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry') # positional arguments
# describe_pet('dog', 'willie') # positional arguments
# # describe_pet('chacha', 'cat') # argument order matters! 

# describe_pet(animal_type='hamster', pet_name='harry') # keyword arguements

describe_pet(pet_name='willie') # default values, animal_type's default value is a 'dog'
describe_pet(pet_name='willie', animal_type='cat') # default value 'dog' is ignored
'''
'''
# a dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# a hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
'''
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()