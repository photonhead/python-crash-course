# make a list of the first 10 square numbers (the square of each integer from 1 through 10)
squares = [] # make an empty list to store values
for value in range(1, 11): # value in range 1 to 10
    square = value ** 2 # square each value
    squares.append(square) # append(add) those square values to the squares list

print(squares) # print the list

''' Be careful with spelling, esp., with singular and plural '''

# more concise code
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# even more concisely!
squares = [value**2 for value in range(1, 11)] # 오오! 그냥 바로 때려넣어버리네. 멋져...
print(squares)

''' 
It feels like a reverse order of thought. It's like English word order. Like, "There's a list called squares. The values in it are the squares of numbers. Those numbers are within this range."
The way of thinking is completely opposite to Korean. In Korean, it would have been "Here're numbers within this range, square them, then placing them in a list called squares." Interesting!
'''