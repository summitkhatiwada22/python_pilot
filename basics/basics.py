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

# there is no limit in integer length or anything in python

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



# STRINGS

my_name = 'Summit Khatiwada'
desc = 'Summit said, "Hi!".'
print(my_name + " " + desc) # This is string concatination
# string concatination can only add string. So you will have to convert int to string before adding.

# multi-line string
essay = '''Hi there
how are you doing?'''
print(essay)

# escape characters
print ('This is a first line. \n This is a second line')
print ('I\'m Summit.')  # to use '

# string length
paragraph = 'a quick brown fox jumpes over the lazy dog.'
print(paragraph.__len__())  # method 1
print(len(paragraph))   # method 2

print(paragraph.capitalize())   # to capitalize
print(paragraph.upper())   # to upper case
print(paragraph.lower())   # to lower case



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


# format method

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


# f-strings
place = 'Kathmandu'
# f strings do not start with quotation but with f
place_2 = f'Pokhara'  # f states that it is a formatted string
destination = f"Our first destination is {place} and second is {place_2}"
print(destination)
age = 55
# padding in fstring
print(f"My age is {age:10d}")
# padding and expression in fstring
print(f"My age is {(age+10):10d}")
print(f"Our first destination is {place.ljust(20)} and second is {place_2.ljust(20)}")
# expression in fstring
print(f"My age is {age + 10}")


# Methods in string
# 1. Finding out the length
name = 'John'
print(len(name))
print(name.__len__())

# 2. Finding data type
age = "12"
print(type(age))

# 3. Checking if the string is numeric
print(age.isnumeric())  # Gives True or False

# 4. Checking if the string is decimal
print(age.isdecimal())  # Gives True or False

# 5. Checking if a word is alphabetic
word = "ABC"
print(word.isalpha())

# 6. Checking if a word is alphanumeric
word = "ABC22"
print(word.isalnum())

# 7. replace method
sentence = 'I am Sam and I am 20 years old.'
new_name = 'Samuel'
print(sentence)
new_sentence = f"I am {new_name} and I am 20 years old."
print(new_sentence)
print(sentence.replace('Sam', new_name)) 
print(sentence.replace('Sam', new_name, 3)) 



# TEXT JUSTIFICATION

# left justification
_mood = 'Jolly'
justified = _mood.ljust(50)
print(justified, 'here')

# left justification with dash ---
_mood = 'Jolly'
justified = _mood.ljust(50, '-')
print(justified, 'here')

# right justification
justified= _mood.rjust(50)
print(justified)

# center alignment
justified= _mood.center(50)
print(justified)

# Download Bar
width = 100
downloaded = 20
bar_content = f'[{("#" * downloaded).ljust(width, ".")}]'
print(bar_content)

# finding the index of a substring
data = 'I am a quite cool.'
print(data.index('cool'))
#checking if it starts with the substring
print(data.startswith('My'))

# trimming spaces
data = '    I am a quite cool.          '
print(data.strip())

#  EXTRACTING SUBSTRING FROM A STRING

text = "Hello, I am john"
# extracting single character
print(text[0])  # gives 'H'
print(text[7])  # gievs 'I'

# it can also be accesed by negative indexing
print(text[-1])  # gievs 'n'

# extracting more than one characters
print(text[0:5])  # gives 'Hello', need to input one more index
print(text[:5])  # gives 'Hello', need to input one more index
print(text[7:]) # gives everything after 7
print(text[-9:-5]) # In negative index, start with smaller number, its opposite
print(text[7:-5]) # Can also use both negative and positive indexing

# extracting substring with step
print(text[0:5:2])  # prints 'Hlo', prinnts in two steps
print(text[::2])
print(text[4::-1]) #reverses the string, olleH
print(text[::-1]) #reverses reverses everything

