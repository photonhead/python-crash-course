'''
8-2. Favorite Book:
Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as 'One of my favorite books is Alice in Wonderland.'
Call the function, making sure to include a book title as an argument in the function call.
'''
# define a function
def favorite_book(title):
    print(f"Your favorite book is {title.title()}.")

title = input("What is your favorite book?: ")
favorite_book(title)