# start
# get miles travelled
# get amount of gallons used
# calculate mileage = miles/gallons
# display results
# stop

miles = float(input("Enter your miles travelled."))
gallons = float(input("How many gallons used for the travel?"))
mpg = miles/gallons
mpg_rounded = round(mpg, 3)

print("You travelled ", miles, "miles.")
print("You used ", gallons, "gallons.")
print("Your mileage is ", mpg_rounded, "mpg.")

# test cases - confirmed by hand
# 100 miles using 4 gallons gives us 25 mpg
# 72.5 miles using 2.8 gallons gives us 25.893 mpg
