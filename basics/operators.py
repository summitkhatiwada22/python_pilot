# OPERATORS

"""
Relational Operations

    equals  (==)
    not equals(!=)
    less than   (<)
    less than or equals (<=)
    greater than    (>)
    greater than or equals  (>=)

Relational operation always returns either True or False
"""

# RELATIONAL - Returns either True or False

# equals (==)
x = 5
print(x == 6)   # returns False
print(x == 5)   # returns True

# Print if a number is odd with relational operator2
a = int(input("Enter any number :: "))
print(f'The number is odd: {a%2 == 1}')

# Print if a number is both divisible by 2 and 3
print('Divisible by both 2 and 3 :: ', a%2 == a%3 == 0)

print("\n\n")


# not-equals (!=)
print(5 != 6)   # returns True
print(5 + 1 != 2 + 4)   # returns False


# Less than (<)
print(4 < 5)    # returns True
print(4 < 4)    # returns False
print(5 < 4)    # returns False
print('A' < 'B') # True

# Less than equals to (<=)
print(4 <= 5)    # returns True
print(4 <= 4)    # returns True
print(5 <= 4)    # returns False

# Greater than (<=)
print(4 > 5)    # returns False
print(4 > 4)    # returns False
print(5 > 4)    # returns True

# Greater than equals to(<=)
print(4 >= 5)    # returns False
print(4 >= 4)    # returns True
print(5 >= 4)    # returns True

# Comparison in strings
print('Ada' < 'B') # True, Checks only first character
print('Ada' < 'A') # False, checks number of characters now, since the first one is same
