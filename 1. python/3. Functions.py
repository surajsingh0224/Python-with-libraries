# write a function to print hello world
'''
def hello_world():
    print("THis is the function called hello world, when i call this funtion the print statement will executed...")

hello_world()
'''

# create a function that takes a name and return "Hello <name>"
'''
def name():
    n = input("Enter your name to greet yourself - ")
    print(f"Hello {n}")
    
name()
'''

# Write a function to add two numbers and return the sum
'''
def addition():
    num1 = int(input("Enter the first number - "))
    num2 = int(input("Enter the second number - "))
    add = num1 + num2
    print(f"The addition of {num1} and {num2} is = {add}")

addition()
'''

# Write a function that takes 3 numbers and returns the largest
'''
def largest():
    num1 = int(input("Enter the first number = "))
    num2 = int(input("Enter the second number = "))
    num3 = int(input("Enter the third number = "))
    
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the greatest...")
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is the gratest...")
    else:
        print(f"{num3} is the gratest...")

largest()
'''

# Create a function that takes a list and returns the first and last elements.
'''
def first_and_last_element(input_list):
    if not input_list:
        return "The input is empty"
    elif len(input_list) == 1:
        return input_list[0], input_list[0]
    else:
        return input_list[0], input_list[-1]
    
    
list_one = [1, 2, 4,  5, 6]
first, last = first_and_last_element(list_one)
print(f"list - {list_one}, first : {first}, last : {last}")
'''

# Write a function that takes a number and returns: square, cube
'''
def square():
    a = int(input("Enter the number you want to square - "))
    result = a * a
    print(f"The square of {a} is - {result}")

def cube():
    a = int(input("Enter the number you want to cube = "))
    result = a * a * a
    print(f"The cube of {a} is ={result}")
    
# square()
cube()
'''

# Write a function that greets a user with default name "Guest"
'''
def greet(name = "guest"):
    print(f"Welcome {name}")
    
greet("Suraj")
'''
# Create a function that calculates area of rectangle. Default width = 1.
'''
def rectangle(length, width = 1):
    return length * width

area1 = rectangle(5, 3)
print(f"The area of the rectangle is = {area1}")
area2 = rectangle(7)
print(f"The area of the rectangle with default width is = {area2}")
'''

# Function to calculate simple interest. Default rate = 10%.
'''
def simple_intrest(principle, time_in_years, rate = 10):
    result = (principle * time_in_years * rate) / 100
    return result

print(simple_intrest(5000, 3, 10))
'''



