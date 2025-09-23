'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Ex 9-3.
Write a method called increment_login_attempts() that increments the value of login_attmepts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly,
and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.
'''
class User:
    """ user information """

    def __init__(self, name, pet_type, pet_name):
        self.name = name
        self.pet_type = pet_type
        self.pet_name = pet_name
        self.login_attempts = 0 # dafault = 0
    
    def describe_user(self):
        print(f"{self.name}'s pet is a {self.pet_type}, and its name is {self.pet_name}.")
    
    def greet_user(self):
        print(f"\"Hi, {self.name}! How are you? How's your {self.pet_type} {self.pet_name} is doing?\"")
    
    def increment_login_attempts(self):
        self.login_attempts += 1 # default 0에서 1씩 증가
        print(f"- Login attempts: {self.login_attempts} times") # call할 때마다 증가한 값으로 보여줌
    
    def reset_login_attempts(self, reset): 
        self.reset = reset
        
        if self.reset == 0: # 이 메서드를 호출할 때 0을 값으로 주면,
            self.login_attempts = reset # 로그인 시도값을 0으로 바꾸고
            print(f"Your login attempt counter has reset. Login attempts: {self.login_attempts} times") # reset results

# create an instance
user1 = User('Sarah', 'dog', 'Beamo')
user1.describe_user()
user1.greet_user()

# call the increment method multiple times to see the increments of login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# call the reset method with value of 0 to reset the login attempts, 
# and then print the reset results, which is 0
user1.reset_login_attempts(0)