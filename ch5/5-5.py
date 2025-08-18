'''
5-5. Alien Colors #3.
Turn your if-else chain from Ex 5-4 into an if-elif-else chain.
- If the aline is green, print a message that the player earned 5 points.
- If the aline is yellow, print a message that the player earned 10 points.
- If the aline is red, print a message that the player earned 15 points.
- Write three versions of this program, makeing sure each message is printed for the appropriate color alien.
'''

# alien_color = 'green' # 5 points
# alien_color = 'yellow' # 10 points
alien_color = 'red' # 15 points

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points! ")