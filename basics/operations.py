# ADDITION
print('ADDITION')

print(5+6)  # adding ints
print(5+6.5)    # adding int and float

x = y = 7
z = 3
print(x+z)  # adding variables

print('Summit' + ' ' + 'Khatiwada')  # adding strings
print((4 + 5j) + (6 + 8j))  # adding complex numbers
print(x, y)  # printing both variables at once

print('')
print('')


# MULTIPLICATION
print('MULTIPLICATION')

print(5*6)  # multiplying ints
print(5*6.5)    # multypling int and float

x = y = 7
z = 3
print(x*z)  # multiplying variables

print('Summit' * 5)  # multiplying strings
print((4 + 5j) * (6 + 8j))  # multiplying complex numbers

print('')
print('')


# DIVISION
print('DIVISION')

print(5/6)  # dividing ints
print(12/3)  # returns in float
print(5/6.5)    # dividing int and float

x = y = 7
z = 3
print(x/z)  # dividing variables

print((4 + 5j) / (6 + 8j))  # dividing complex numbers


# integer division
print(5//2)  # returns integer only, returns 2
print(5.2//6.5)  # returns integer only
print(45.8//5.1)    # first divides and then removes the decimal to 0

print('')
print('')


# MODULUS
print('MODULUS')

print(9 % 4)  # returns the remainder, 1
print(25 % 3)  # returns the remainder, 1

# use cases - to find odd or even
print(3232345 % 2)    # returns 1, hence odd

# use cases - load balancing
total_computers = 5
guest_roll = 2345677499
print(guest_roll % total_computers) # remainder is 4, hence sends to computer number 4

print('')
print('')


# EXPONENTIATION
print('EXPONENTIATION')

# syntax: x ** y
print(2 ** 7)
print(5 ** 3)
print(pow(2, 7))
