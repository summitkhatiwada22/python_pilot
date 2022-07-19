# USER INPUT

# no need to print input statement, only write print
# input takes str4ing, a number entered is taken in string

x = input('Enter any number:')

print(type(x))  # shows the input type of number is a string

print(f'You entered {x}')

# type casting - converting the data type
x = int(x)
print(type(x))
print(f'Square = {x ** 2}')
print(f'The cube of {x} = ', x ** 3)

# input within print statement
print(f'Total = {int(input("First Number = ")) + int(input("Second Number = "))}')
