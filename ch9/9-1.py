'''
9-1. Restaurant: Make a class called Restaurant.
The __init__ () method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods.
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type): # two attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self): # a method prints two pieces of information
        print(f"{self.restaurant_name} is {self.cuisine_type} cuisine.")
    
    def open_restaurant(self, open): # a method prints a msg indicating the retaurant is open
        self.open = open
        print(f"They are {self.open} today.")

# make two instances
fav1_cuisine = Restaurant('Panda Express', 'Chinese')
fav2_cuisine = Restaurant('Lil Woody\'s', 'American')

# print two attributes individually
print(f"One of my favorite restaurants is {fav1_cuisine.restaurant_name}, and it's {fav1_cuisine.cuisine_type} cuisine.")
print(f"My second choice is {fav2_cuisine.restaurant_name}, and it's {fav2_cuisine.cuisine_type} cuisine.\n")

# call both methods
fav1_cuisine.describe_restaurant()
fav1_cuisine.open_restaurant('closed')

fav2_cuisine.describe_restaurant()
fav2_cuisine.open_restaurant('open')