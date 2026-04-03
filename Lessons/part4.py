# data types!
# string data type
# literal assignment
import math
first = "Kali"
last = "Faiz"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor funtion
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(2000)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
hey, how are you?                                        

I was just gooning to majids picture under my pillow!   
                    All good?

'''
print(multiline)

# Escaping special characters
# \t indicates a tab
# \n indicates a new line
# to escape a backwards slash, use two, \\

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located'
print(sentence)

# String methods, are methods that call on the string class.
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                    "
multiline = "           " + multiline 
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "£1".rjust(4))
print("Muffin".ljust(16, ".") + "£2".rjust(4))
print("Cheesecake".ljust(16, ".") + "£4".rjust(4))
#ljust = left justify
#rjust = right justify



# string index values
print(first[1])
print(first[-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("K"))
print(first.endswith("i"))

# Boolean data type
myvalue = True 
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types
# interger type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, bool))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))


# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorect data.
# zip_value = int("New York")




