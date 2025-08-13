# start

# allocate three values to variables.
a = 7
b = 2.5
c = 18

# define the list of calculations
all_calculations = [
    3 * 12 - 7,
    3 * (12 - 7),
    a * b + 2,
    a * ( b + 2.5 ),
    c % 4,
    (a + c) % 4,
    a + c % 4,
    a + b * 2,
    c // 4,
    16 / 4 / 2,
    c / 4,
    a**2,
    int(b),
    float(a + c),
    a % 2,
    c % 2,
    4 ** 3 + 1,
    25 ** 0.5,
    8** 1 / 3,
    8 ** (1/3)
]

# print the results line by line.
print(all_calculations)
