# touch <filename>
# creates a file in the scurrent directory

# pwd
# shows the current working directory

# echo <content>
# displays the content

# echo (content) > <filename>
# saves the content in the filename

# mv <old_filename> <new_filename>
# rename filename

# rm <filename>
# deletes particular file

# rm -r <foldername>
# deletes the filder and all it's content

# use option and click where to write to write in multiple places at once

# there is no limit in integer length or anything in python

# git log --oneline -> to see all commits in one line

# option+shift+down arrow -> copies the same line down

# git rm --chached course/c01   -> to ignore already tracked file. Use --cached otherwise local will also be delered

# PRTINTING

print("hello world")


# VARIABLES
# checkout PEP for python standards
x = 5       # x <- 5, x is an identifier storing 5 for now
_x = 50     # variables startingwith _ are protected

name = 'Summit'     # lower case
NAME = 'Summit'     #  upper case
nameOne = 'Khatiwada'   # lower camel case
NameOne = 'Khatiwada'   # upper camel case

# snake case, this is a python standard
name_one = 'Summit Khatiwada'   # use _ to separate variables


# CONSTANTS
# use upper case variable to make it a constant
# its just a convention, the value can be changed, but dont change
PI = 3.1415
PROJECT_VERSION = '1.0.0'
COMPANY_NAME = 'The Vedic Medic LLC'


# DATA TYPES
# NUMERIC DATA TYPES

# integer
x = 6
y = -6

# binary representation
bin_1 = 0b1010
bin_2 = 0b110011
print(bin_1)
print(bin_2)

# octal representation
oct_1 = 0o1574
print(oct_1)

# hexadecimal representation (hex)
hex_1 = 0x2df2
print(hex_1)

# floating point
z = 5.5
total_score = 67.58

# complex numbers
# these are the numbers with i
# a + bi
# eg. 1 + 2i, 1 + 3j -> i and j are used
# i or j can also be used in the front like 1 + i2
val_1 = 1 + 2j  # j is standard in python
val_2 = 1 + 0j  # this does not have the imaginary part
val_3 = -5j     # this does not have real part
val_4: complex = 8 + 89j    # using : is just for type hinting, its just for us to understand

# boolean data type
# all other languages have true/ false while python has True/False
married = False
is_student = True
internet_status = True
retired = False


###
# TODO - Missed string session here. Complete them.

# string concatination can only add string. So you will have to convert int to string before adding.
###


# STRING FORMATTING
age = 20    # %d for int - %[a]d
height = 6.0    # %f for float - %[a].[b]f
f_name = 'Summit'   # %s for string
l_name = 'Khatiwada'

# usual method
full_name = f_name + ' ' + ' ' + l_name
print(full_name)

# using %s, %d, %f
full_name_2 = "My name is %s %s. I am %d years old and my height is %f." %(
    f_name, l_name, age, height)
print(full_name_2)

weight = 170.567
print("My weight is %5.2f" %weight)    # using %[a].[b]f, a is the preceeding spaces, its called space padding
print("My weight is %5.2f" %weight)    # using %[a].[b]f, a is the preceeding spaces, its called space padding


# FORMAT METHOD

# templating
# we use curly bracket for adding a placeholder
name = 'Summit Khatiwada'
address = 'Indiana'
number = 12
# option 1
print('My name is {}. I live in {} and my lucky number is {}'.format
(name, address, number))

# option 2
print('My name is {full_name}. I live in {add} and my lucky number is {num}'.format
(full_name=name, add=address, num=number))

# option 3 - padding
print('My name is {full_name}. I live in {add} and my lucky number is {:5d}'.format
(number, full_name=name, add=address))
 
 # option 4 - right padding, use > or :-> or :+>8d
print('My name is {full_name}. I live in {add} and my lucky number is {:->5d}'.format
(number, full_name=name, add=address))


