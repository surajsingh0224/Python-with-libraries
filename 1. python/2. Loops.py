# for loop questions
'''
n = int(input("Tell your number - "))
for i in range(n):
    print(f"{i} \t HEllO WORLD")
    '''

# print natural numbers to n
'''
n = int(input("PLease tell the number - "))
for i in range(1, n+1):
    print(i)
    '''
    
# Reverse for loop. Print n to 1 
'''
n = int(input("PLease tell the number - "))
for i in range(n, 0, -1):
    print(i)
   '''
   
# Take a number as input and print its table 
'''
n = int(input("PLease tell the number - "))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
'''

#  Sum up to n terms
'''
n = int(input("PLease tell the number - "))
sum = 0
for i in range(1, n+1):
    sum = sum+i
print(f"Sum of the number {n} is {sum}")
   '''
   
# Factorial of a number 
"""
n = int(input("PLease tell the number - "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f"Factorial of {n} is {fact}")
"""

# Print the sum of all even & odd numbers in a range separately
'''
n = int(input("tell your number = "))
even = 0
odd = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print(f"Your even and odd sum are {even} , {odd}")
'''

# Print all the factors of a number 
'''
n = int(input("tell your number = "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
'''

# Accept a number and check if it a perfect number or not.
'''
n = int(input("tell your number = "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + 1
if sum == n:
    print("Your number is perfect...")
else:
    print("Not a perfect number...")
'''
'''
n = int(input("Check number prime or not = "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count = count + 1
        
if count == 2:
    print("your number is prime")
else:
    print("Number is not prime")
'''

# Reverse a string without using in build functions.
'''
a = "suraj"
b = ""
for i in range(len(a)-1, -1, -1):
    b = b + a[i]
print(b)    
'''





