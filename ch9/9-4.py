'''
9-4. Number Served: Start with your program from Ex 9-1.
Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class.
Print the number of customers the restaurant has served,
and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who've been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business.
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type): 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # add a new attribute, default value of 0

    def describe_restaurant(self): 
        """Prints the restaurant name and its cuisine type."""
        print(f"{self.restaurant_name} is {self.cuisine_type} cuisine.")
    
    def open_restaurant(self, open): 
        """Prints a msg indicating the retaurant is open."""
        self.open = open
        print(f"They are {self.open} today.")

    def num_served(self):
        """Prints the number of customers the restaurant has served."""
        print(f"This restaurant had {self.number_served} customer on the first day.")

    def update_num_served(self, update_num_served):
        """Prints the updated number of customers the restaurant has served."""
        self.update_num_served = update_num_served
        print(f"Soon, this restaurant has served {self.update_num_served} customers!")

    def set_num_served(self, set_num_served):
        """Set the number of customers that have been served."""
        self.set_num_served = set_num_served
        print(f"This restaurant has been served {self.set_num_served} times so far!")

    def increment_number_served(self, incre_num_served):
        """Increment the number of customers who've been served."""
        self.set_num_served += incre_num_served
        print(f"Amazingly, this restaurant served {incre_num_served} customers today, so now they has been served {self.set_num_served} customers in total!")

restaurant = Restaurant('Olive Garden', 'Italian') # create an instance 
restaurant.describe_restaurant() # print its information

# Print the number of customers the restaurant has served. (default = 0)
restaurant.num_served() 

# Change its value and print it again. (served num = given number)
restaurant.update_num_served(34_500)

# Call this method with a new number and print the value again.
restaurant.set_num_served(21_367)

# Call this method with any number that represent how many customers were served in a day.
restaurant.increment_number_served(789)