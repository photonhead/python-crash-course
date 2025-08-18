'''
5-1. Ordinal Numbers:
- Store the numbers 1 through 9 in a list.
- Loop through the list.
- Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
'''
# make a list range from 1 to 9
cardinal_numbers = list(range(1,10))

# loop throught the list
for number in cardinal_numbers:
    if number == int(1): # comparing numbers, in case 1
        print("1st")
    elif number == int(2): # comparing numbers, in case 2
        print("2nd")
    elif number == int(3): # comparing numbers, in case 3
        print("3rd")
    else:
        print(f"{number}th") # comparing numbers, other cases