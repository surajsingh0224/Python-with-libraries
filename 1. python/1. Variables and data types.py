# Create a variable a, b, c to store your name, age and height

a = "Suraj kumar singh"
b = "19"
c = "5,10."

print(f"My name is {a}. my age is {b}. my height is {c}")


# Swap the two numbers with and without using third variable

a = 12
b = 13
temp = 0

print("Swapping of two numbers with using third variable - ")
print(f"Before swapping - {a} and {b}")
temp = a
a = b
b = temp
print(f"after swapping - {a} and {b}")

print("Swapping of two numbers without using third variable -")

c = 23
d = 32
print(f"Before swapping - {c} and {d}")
c = c+d
d = c-d
c = c-d
print(f"After swapping - {c} and {d}")
'''

# give a string s = "123" and convert it into int, float and bool and print its types
'''
string = "123"
inte = int(string)
print(f"String to integer - {inte}", type(inte))

flo = float(string)
print(f"String to float - {flo}", type(flo))

boo = bool(string)
print(f"String to bool - {boo}", type(boo))
'''

# Take the user input for two numbers and print - sum, difference and the type of the input
'''
first_number = int(input("Enter the first number = "))
second_number = int(input("Enter the second number = "))
add = first_number + second_number
print(f"The addition of the {first_number} and {second_number} are = {add}")
print(f"The input type of add = {type(add)}")
difference = first_number - second_number
print(f"the difference of {first_number} and {second_number} are = {difference}")
print(f"The input type of difference = {type(difference)}")
'''

# what is the output of this code - 
'''
x = "10"
y = 5
print(x * y)
'''

# x = "10"
# y = 5
# print(x * y)

# ans - 10 will be printed 5 times

# create a variable marks = 89.9999 and convert it into - int, rounded int and string
'''
marks = 89.9999
inte = int(marks)
print(f"Converted to int = {inte} and type is = {type(inte)}")
r_int = round(marks)
print(f"Convert to rounded int = {r_int} and type is = {type(r_int)}")
string = str(marks)
print(f"Convert to string = {string} and type is = {type(string)}")
'''

# predict the output 
'''
a = 10
b = a
a = 20
print(a, b)
'''

# python treats everything as an object. prove it by printing id() of a variable before and after changing its value
'''
var = 10
print(f"Initial value of var is {var}")
print(f"ID of the object is refered to by var = {id(var)}")
'''

# Explain what happens here = 
'''
a = "5"
b = int(a) + float(a)
print(b)
# THe a is firstly converted string to int and added to float which converts a (string) into floating point number
'''

# What is the output
'''
a = True
b = 1
print(a + b)
# In bool True indicates 1. so True + 1 is 2
'''

# why does this works
'''
print("Hello" * 3)
'''
# Because the string is multiplied 3 times


# check if the variable x is integer without using type function
# total 5 methods
'''
p = 10
print("Method 1 - ")
if isinstance(p, int):
    print("p is an integer...")
else:
    print("p is not an integer...")
    
print("Method 2 -")
q = 10.0
if isinstance(q, float) and q.is_integer():
    print("q behaves like an integer...")
    
print("Method 3 - ")
r = 10
if r % 1 == 0:
    print("r is an integer...")
else:
    print("r is not an integer...")
    
print("Method 4 - ")
s = 10
if int(s) == s:
    print("s is an integer...")
else:
    print("s is not an integer...")

print("Method 5 - ")
t = 10
if isinstance(t, (int, float)) and t == int(t):
    print("t is an integer...")
'''

# Why does b not change
'''
a = "python"
b = a
a = "java"
print(a, b)
'''

# Convert this into int(with round rules), float and then multiply by 2 and print output with data types
'''
values = "89.97"
value_float = float(values)
print(f"Converted string to integer = {value_float * 2} {type(value_float)}")
# round the value_float
print(f"The round of the value_float is - {round(value_float) * 2}  {type(value_float)}")



