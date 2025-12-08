'''
# Create a Laptop class
# Attributes: brand, RAM, storage
# Constructor should set all values
# Method: info() → prints details

class Laptops:
    def __init__(self, brand, ram, storage): # this is a instance attribute
        self.brand = brand
        self.ram = ram
        self.storage = storage
    
    def info(self): # this is a method that show the output 
        print(f"The specifications of laptop is {self.brand} Ram is {self.ram} and the the storage is {self.storage}")

brand = input("Which brand is your laptop ? ")
ram = input("What is the requirment of the ram ? ")
storage = input("How much of storage you want ?")
obj = Laptops(brand, ram, storage)
obj.info()
'''
'''
class Student:
    def __init__(self, name, roll_number, marks):
         self.name = name
         self.roll_number = roll_number
         self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def student_info(self):
        avg_marks = self.average()
        if avg_marks >= 90:
            print("A grade")
        elif avg_marks >= 75:
            print("B grade")
        else:
            print("C grade")
            
        print(f"Name : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Average marks : {avg_marks: .2f}")

name = input("Enter your name : ")
roll = input("Enter your roll number : ")

marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i} : "))
    marks.append(m)

obj = Student(name, roll, marks)
obj.student_info()
'''

'''
class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount !!!")
            return
        self.balance = self.balance + amount
        print(f"{amount} Deposited Sucessfully !!!")
        
    def withdraw(self, amount):
        if amount <= 0:
            print(f"Invalid Withdrawal Amount")
            return
        if amount > self.balance:
            print("Insufficiant balance...")
            return
        self.balance = self.balance - amount
        print(f"{amount} Withdrawal sucessfully...")
        
    def check_balance(self):
        print(f"Current balance for {self.name} : {self.balance}")


account = BankAccount("Suraj", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.check_balance()
'''
'''
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        if length < 0:
            print("Invalid length... Setting to 0.")
            self.length = 0
            
        if width < 0:
            print("Invalid width... Setting to 0.")
            self.width = 0
            
    def area(self):
        return self.length * self.width
        
        
    def perimeter(self):
        return 2 * (self.length + self.width)
          
    def info(self):
        print(f"The area of the rectangle is {self.area()} and the perimeter of the rectangle is {self.perimeter()}")
        
obj = rectangle(-10, 5)    
obj.area()
obj.perimeter()    
obj.info()
'''

'''
class PasswordManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def update_password(self, old_pass, new_pass):
        if self.password == old_pass:
            self.password = new_pass
            print("Password updated sucessfully...")
        else:
            print("Incorrect password... Try again")
            
    def is_strong(self):
        if len(self.password) < 8:
            return False
        contains_digit = any(ch.isdigit() for ch in self.password)
        return contains_digit
      
    def info(self):
        strength = "strong" if self.is_strong() else "weak"
        print(f"Username = {self.username}")
        print(f"password strength = {strength}")
        
        
user = PasswordManager("suraj", "abc123")
user.update_password("abc123", "hello1234")
user.info()
'''
















  
        
        
        
        







