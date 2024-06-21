# string data type

# literal assignment
first = 'Maria'
last = 'Buzing'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#Concatenation
fullname = first +  " " + last
print(fullname)

fullname += "!"
print(fullname)

#Casting a number to a string
decade = str(2000)
print(type(decade))
print(decade)

statement = " I was born in the " + decade + " s. "
print(statement)

# Multiple lines
multiline = """
Hey, how are you?

I was just checking in.

                        All good?

"""
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                          "
multiline = "                             " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print(" ")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print(" ")

# string index values
print(first[0])   #first value
print(first[1])   #second value
print(first[-1])  #last value
print(first[1:-1])   #value at the end of the range does not give you an output
print(first[1:])   #second through last value


# some methods return boolean data
print(first.startswith("M"))
print(first.endswith("z"))

#boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# numeric data types

#integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers
print(abs(gpa))  #absolute value
print(round(gpa))  #rounded value
print(round(gpa, 1))  #rounded to the 1st decimal place

import math

print(math.pi)

print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number

zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#error if you attempt to cast incorrect data
# zip_value = int("New York")

