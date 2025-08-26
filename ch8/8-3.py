'''
8-3. T-Shirt:
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
- Call the function once using positional arguments to make a shirt.
- Call the function a second time using keyword arguments.
'''
# define a function
def make_shirt(size, text):
    print(f"Your T-shirt size is '{size.upper()}'. We will print '{text}' on your T-shirt.")

# call the function using positional arguments
make_shirt('m', 'Python is Fun!')

# call the function using keyword arguments
make_shirt(size='l', text='Function is Insteresting!')