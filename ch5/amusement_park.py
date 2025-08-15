# if-elif-else chain
age = int(input("What is your age?: "))

'''
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
'''
'''
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20 # age >= 65: price = $20 

print(f"Your admission cost is ${price}.")
'''

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20 # 아예 65세 이상은 20불이라고 지정함으로써 모든 범위를 커버하므로
# else 문이 필요없으니 생략 가능!

print(f"Your admission cost is ${price}.")