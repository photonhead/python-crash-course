'''
6-1. Person: Use a dictionary to store information about a person you know.
Store their first and last name, age, the city they live in. 
You should have keys such as first_name, last_name, age, and city.
Print each piece of information stored in your dictionary.
'''
person_info = {
    'first_name': 'sarah',
    'last_name': 'young',
    'age': '36',
    'city': 'austin'
}

message = (f"One of my best friends is {person_info['first_name'].title()} {person_info['last_name'].title()}. She is {person_info['age']} years old and lives in {person_info['city'].title()}.")

print(message)