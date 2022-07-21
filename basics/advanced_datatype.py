# ADVANCED DATATYPE

# LIST
# TUPLE
# SET
# DICTIONARY


# LIST
# Collection of data, separated by , and enclosed in []

list_1 = [5,6]
print(list_1)
print(type(list_1))

students = ['Amit', 'Ava', 'Chan']
print(students)

# accessing
print(students[0])  # Amit
print(students[1])  # Ava
print(students[2])  # Chan

# list can have more than one fata type
mess = [1, 1.5, 'Ola', True]
print(mess[0])
print(mess[1])
print(mess[2])

# list can use negative indexing
print(mess[-1])
print(students[-2])

# you can use ',' in the end of the list and can also make list multiline
animals_1 = [
    'cat',
    'dog',
    'tiger',
]

print(animals_1[-1]) # gives tiger
print(animals_1[0:2]) # subset of list, also calles SLICE



