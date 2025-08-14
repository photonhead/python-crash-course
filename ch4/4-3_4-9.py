# 4-3. Counting to twenty: use a for loop to print the numbers from 1 to 20, inclusive.
# for number in range(1, 21):
#     print(number)

# 4-4. One million: Make a list of the numbers from 1 to 1 million, and then use a for loop to print the numbers. If output is taking too long, stop it by pressing Ctrl-C or by closing the output window.
# 1 million is too large, so I'm going to change it to 100.
# numbers = [value for value in range(1, 101)]
# print(numbers)

'''
4-5. Summing a million: 
Make a list of the numbers from 1 to 1 million, and then use min() and max() to make sure your list actually starts at one and ends at one million. also, use the sum() function to see how quickly python can add a million numbers.

numbers = [value for value in range(1, 1000001)]
print(f"range: 1 to million, min: {min(numbers)}, max: {max(numbers)}, sum: {sum(numbers)}")
'''
'''
# 4-6. Odd numbers: use the third argument of the range() function to make a list of the odd numbers from 1 to 20. use a for loop to print each number.
odds = [num+1 for num in range(0, 20, 2)]
for value in odds:
    print(value)
'''

# 4-7. Threes: Make a list of the multiple of 3, from 3 to 30. use a for loop to print the numbers in your list.
numbers = []

for num in range(1, 11):
    multiple = num * 3
    numbers.append(multiple)

print(numbers)

# can i make it more concise?
numbers = [num*3 for num in range(1, 11)]
print(numbers)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes, and use a for loop to print out the value of each cube.
cubes = [num**3 for num in range(1,11)]
for value in cubes:
    print(value)

# 4-9. Cube Comprehension: use a list comprehension to generate a list of the first 10 cubes.
cubes = [num**3 for num in range(1,11)]
print(cubes)