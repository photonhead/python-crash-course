'''
8-4. Large Shirts:
Modify the make_shirt() function so that shirts are large by default with a message that reads 'I love Python'. 
Make a large shirt and a medium shirt with the defualt message, and a shirt of any size with a different message.
'''
# modify make_shirt() function
def make_shirt(size='L', text='I love Python'):
    print(f"Your T-shirt size is '{size.upper()}'. We will print '{text}' on your T-shirt.")

# make a larget shirt with the default message
make_shirt()

# make a medium shirt with the default message
make_shirt('m')

# make a shirt of any size with a different message
make_shirt('s', 'Who is Monty Python?')