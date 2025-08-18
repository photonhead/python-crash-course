'''
5-10. Checking Usernames:
Do the following to create a program that simulates how websites ensure that everyone has a unique username.
- Make a list of five or more usernames called 'current_users'
- Make another list of five usernames called 'new_users'. Make sure one or two of the new usernames are also in the current_users list.
- Loop through the new_users list to see if each new username has already been used. If is has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
- Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you'll need to make a copy of current_users containing the lowercase versions of all existing users.)
'''

current_users = ['sarah', 'alex', 'Krystle', 'JASON', 'michael'] # 소문자, 일부 대문자, 전부 대문자로 된 사용자 이름이 섞여 있다.
new_users = ['ALEX', 'dani', 'luci', 'joe', 'krystle'] # 마찬가지로 대소문자가 섞여 있다.

# create a lowercase copy of the current_users list 
# 대문자가 사용자 이름의 일부 또는 전체일 수 있으므로 대문자로 바꿔서는 확인이 불가하다. 따라서 전부 다 소문자로 바꾸어 비교하면 모든 경우를 확인할 수 있다.
current_users_lower = [current_user.lower() for current_user in current_users]
print(current_users_lower) # 제대로 복사되었는지 확인용

for new_user in new_users: 
    # convert the new username to lowercase for the case-insensitive check
    if new_user.lower() in current_users_lower: 
        print(f"{new_user} is already taken. Please use another username.")
    else: 
        print(f"{new_user} is available!")