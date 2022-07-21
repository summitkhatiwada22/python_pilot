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
from asyncio.proactor_events import _ProactorBaseWritePipeTransport


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

print("\n\n")


# INSERT LOGICAL GATES HERE - MISSED A CLASS HERE
# INSERT LOGICAL GATES HERE - AND OR NOT
"""
Logical Operators
- logical operators are used to combined 2 or more relational operators or conditions
- They use human readable words as operators
    - and
    - or
    - not
"""
# INSERT LOGICAL GATES HERE
# INSERT LOGICAL GATES HERE
# INSERT LOGICAL GATES HERE


# BITWISE OPERATORS

"""
# Bitwise Operators

- bitwise operators, as suggested by name, work on bit.
- bitwise operator works only with numeric values
- operation is done with each bit position rather than the value as a whole
- suppose we have 2 numbers `5` and `6`
We need to understand binary to decimal conversion and vice versa to understand bitwise operation

binary numbers are also known as base-2 numbers

** not just valid for python

- `5` in decimal is `101` in binary
- `16` in decimal is `10000` in binary

for uint8 or u8,

5   =   0 0 0 0    0 1 0 1
16  =   0 0 0 1    0 0 0 0

for uint32 or u32,

5   =   `0000 0000 0000 0000 0000 0000 0000 0101`

16  =   `0000 0000 0000 0000 0000 0000 0001 0000`

in the above example, we perform bitwise operation to same positioned digit
of the both numbers
    - the first digit of the first value interacts with the first digit of second value
    - the second digit of the first value interacts with the second digit of second value,
      ...
    - the last digit of the first value interacts with the the last digit of second value

you can always check the binary value of a number with
`bin()` function.


Some Bitwise Operations

- Bitwise AND operator `&`
- Bitwise OR operator `|`
- Bitwise NOT operator `~`
- Bitwise XOR operator `^`
- Bitwise SHIFT LEFT operator `<<`
- Bitwise SHIFT RIGHT operator `>>`

"""

a = 5
b = 16

print(a and b)  # gives 16 - Logical operator
print(a & b)    # gives 0
print(a | b)    # gives 21
print(~a)   # NOT operator, gives -6
print(a^b)  # XOR operator, gives 21
print(9 << 1)   # Left shifts, gives 18
print(9 >> 1)   # Right shifts, gives 4






