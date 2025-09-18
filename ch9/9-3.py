'''
9-3. Users: Make a class called User.
Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user's information.
Make another method called greet_user() that prints a personalized greeeting to the user.
Create several instances representing different users, and call both methods for each user.
'''
# make a class
class User:
    """ user information """

    def __init__(self, name, pet_type, pet_name):
        self.name = name
        self.pet_type = pet_type
        self.pet_name = pet_name
    
    def describe_user(self):
        print(f"{self.name}'s pet is a {self.pet_type}, and its name is {self.pet_name}.")
    
    def greet_user(self):
        print(f"Hi, {self.name}! How are you? How's your {self.pet_type} {self.pet_name} is doing?")

# create several instances
user1 = User('Sarah', 'dog', 'Beamo')
user2 = User('Alex', 'cat', 'Freya')
user3 = User('Jason', 'dog', 'Khai')

# call both methods for each user
user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()