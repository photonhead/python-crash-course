'''
5-4. Alien Colors #2.
Choose a color for an alien as you did in Ex 5-3, and write an if-else chain.
- If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
- If the alien's color isn't green, print a statement that the player just earned 10 points.
- Write one versions of this program that runs the if block and another that runs the else block.
'''

# create a variable and assign it a value of colors.
alien_color = 'green' # 5 points
# alien_color = 'yellow' # 10 points
# alien_color = 'red' # 10 points

if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points! ")