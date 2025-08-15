'''
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
'''

# my food list, and copy my list for my friend's food list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# add a different food to each list 
my_foods.append('cannoli')
friend_foods.append('ice cream')

# print each list using for loop so each food can be listed in each
print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())