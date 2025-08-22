'''
6-6. Polling: Use the code in favorite_languages.py
- Make a list of people who should take the favorite languages poll. 
Include some names that are already in the dictionary and some that are not.
- Loop through the list of people who should take the poll. 
If they have already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take the poll.
'''
# make a list of people who should take the favorite languages poll.
poll_targets = ['jen', 'sarah', 'edward', 'phil', 'jason', 'alex']

# bring the dictionary from favorite_languages.py file
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# loop through the list of people who should take the poll
for user in poll_targets:
    if user in favorite_languages.keys(): # user who have already taken the poll
        print(f"{user.title()}, thank you for taking the poll!")
    else: # user who haven't yet taken the poll
        print(f"{user.title()}, please take our poll.")