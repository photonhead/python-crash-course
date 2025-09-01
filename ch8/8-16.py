'''
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import * 
'''
# a file has one function - pizza.py 
# make_pizza(size, *toppings) function

"""import pizza 
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')"""

"""from pizza import make_pizza
make_pizza(9, 'tomato', 'mushrooms', 'black olives', 'sausage')"""

"""from pizza import make_pizza as mp
mp(16, 'basil', 'mozzarella cheese', 'tomatoes')"""

"""import pizza as pz
pz.make_pizza(9, 'goat cheese', 'artichoke', 'cream sauce', 'roasted garlic')"""

from pizza import *  ### <-- Not Recommended, tho!
make_pizza(20, 'combination')