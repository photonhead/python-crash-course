'''
5-9. No users:
Add an if test to hello_admin.py to make sure the list of users is not empty.
- If the list is empty, print the message 'We need to find some users!'
- Remove all of the usernames from your list, and make sure the correct message is printed.
'''
# usernames = ['Sarah', 'Jason', 'Alex', 'Krystle', 'admin', 'Dani', 'Luci']
usernames = []

# check whether the list is empty or not:
if usernames: # if it's True (= the list is NOT empty)
    for username in usernames: # get a username from the list
        if username == 'admin': # check if it's 'admin'
            print("Hello admin, would you like to see a status report?")
        else: # if username is not 'admin'
            print(f"Hello {username}, thank you for logging in again.")
else: # if it's False (= the list IS empty)
    print("We need to find some users!")