# 함수가 저장되어 있는 파일 pizza.py를 모듈(module)이라 부른다.
# 함수를 호출할 때는 1) 모듈을 먼저 import하고 (이때, 파일명만 쓰면 됨),
# 2) '모듈명.함수명(인수)'로 call하면 된다.
'''
import pizza 

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
'''
# importing a specific funcion from a module 
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
'''
# using an alias for a specific function
from pizza import make_pizza as mp 

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
# giving a module an alias directly
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')