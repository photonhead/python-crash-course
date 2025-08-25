pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

'''
# When I want to remove the repetitive pets only from the list:
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

pets = set(pets)
print(pets)
'''