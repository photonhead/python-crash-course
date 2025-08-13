'''
3-1. Names: Sotre the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.

3-2. Greetings: With the name list, print a message to them printing each person's name. Each message should be the same but each message should be personalized with the person's name.

3-3. Your Own List: Favorite transportation list, such as a motorcycle or a car. Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle."
'''

'''
names = ['nogi', 'sarah', 'krystle', 'dani', 'lucy', 'ila', 'cait', 'alex']

print(names[0].title()) # Nogi
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())
print(names[6].title())
print(names[7].title()) # Alex

print("Hi,", names[3].title() + "! How are you doing? I miss you!") 
# output: "Hi, Dani! How are you doing? I miss you!"
'''

transportations = ['scooter', 'bus', 'car', 'train', 'plane', 'boat', 'ferry']

print(transportations[0].upper() + " is one of my favorite transporatation and I would like to own a Vespa someday!")
print(transportations[3].title() + " is fun to ride, but I prefer to drive a " + transportations[2].lower() + ".")