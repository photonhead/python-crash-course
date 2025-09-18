'''
9-2. Three Restaurant: Start with your class from Ex 9-1.
Create three different instances from the class, and call describe_restaurant() for each instance.
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type} cuisine.")
    
    def open_restaurant(self, open):
        self.open = open
        print(f"They are {self.open} today.")

# create three different instances from the class
fav1_cuisine = Restaurant('Panda Express', 'Chinese')
fav2_cuisine = Restaurant('Lil Woody\'s', 'American')
fav3_cuisine = Restaurant('Mario\' Pizza', 'Italian')

# call describe_restaurant() method for each instance
fav1_cuisine.describe_restaurant()
fav2_cuisine.describe_restaurant()
fav3_cuisine.describe_restaurant()

print("\nThese are my favorite restaurants!")