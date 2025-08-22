'''
6-7. People: Start with the program you wrote for Ex 6-1.
Make two new dictionaries representing different people, and store all three dictionaries in a list called 'people'. 
Loop through your list of people. As you loop through the list, print everything you know about each person.
'''
# make three dictionaries representing different people
user_0 = {
    'ysarah': {
        'first_name': 'sarah',
        'last_name': 'young',
        'age': 35,
        'city': 'austin'
    }
} 

user_1 = {
    'ldani': {
        'first_name': 'dani',
        'last_name': 'lorentzen',
        'age': 29,
        'city': 'port angeles'
    } 
}

user_2 = {
    'smichael': {
        'first_name': 'michael',
        'last_name': 'smythies',
        'age': 30,
        'city': 'seattle'
    }
}

# make a list called 'people' storing all three dictionaries
people = [user_0, user_1, user_2]

# loop through the 'people' list and print all info for each person
for user in people:
    for username in user.keys():
        print(f"Username: {username}")

        for user_info in user.values():
            full_name = f"{user_info['first_name']} {user_info['last_name']}"
            print(f"- Full name: {full_name.title()}")
            
            print(f"- Age: {user_info['age']}")
            print(f"- Location: {user_info['city'].title()}")