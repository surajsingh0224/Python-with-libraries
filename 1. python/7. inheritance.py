# Inheritance in python
# class parent:
#     def speak(self):
#         print("I can speak...")
        
# class child(parent):
#     pass

# obj = child()


# class Parent:
#     def __init__(self, name):
#         self.name = name
        
# class Child(Parent):
#     def display(self):
#         print(f"My name is {self.name}")

# obj = Child("Suraj")
# obj.display()

# Using super function for parent class
# class Parent:
#     def __init__(self, name):
#         self.name = name
        
# class child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
        
#     def display(self):
#         print(f"My name and age is {self.name}, {self.age}")

# obj = child("Suraj kumar singh", 19)
# obj.display()


# program using multiple inheritance
# class Father:
#     def DadSkills(self):
#         print("Coding")

# class Mother:
#     def MomSkills(self):
#         print("Cooking")

# class child(Father, Mother):
#     def show(self):
#         print("I have both Skills -")
#         self.MomSkills()
#         self.DadSkills()

# obj = child()
# obj.show()

# program using multilevel inheritance
# class GrandParent:
#     def heritage(self):
#         print("Heritage from the grand parent")
        
# class parent(GrandParent):
#     pass

# class chid(parent):
#     pass


# class Vehicle:
#     def __init__(self, brand, model):
#          self.brand = brand
#          self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, seat):
#         super().__init__(brand, model) 
#         self.seat = seat
    
#     def display(self):
#         print(f"The brand of the car is {self.brand}, model is {self.model} and the number of seats are {self.seat}")


# brand = input("Enter the brand of the car = ")
# model = input("Enter the model of the car = ")
# seats = input("Enter the number of seats = ")

# obj = Car(brand, model, seats)
# obj.display()

# class person:
#     pass

# class Student(person):
#     def display(self):
#         print("Iam studying...")

# obj = person()


# import math as mt
# class Shape:
#     def area(self):
#         print("Sub classes must implement parent class")
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         print(f"The area of the circle is = {mt.pi * (self.radius ** 2)}")
    
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
        
#     def area(self):
#         print(f"The area of the square is = {self.side ** 2}") 
    
# obj = Circle(5)
# obj.area()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, rollNo):
#         super().__init__(name, age)
#         self.rollNo = rollNo
        
#     def display(self):
#         print(f"The name of the student is {self.name}, age is {self.age} and Roll number is {self.rollNo}")
        
# name = input("Enter your name = ")
# age = input("Enter your age = ")
# rollNo = input("Enter your roll No =")
# obj = Student(name, age, rollNo)
# obj.display()


# class Animal:
#     def eat(self):
#         print("I love to eat chicken...")
        
# class Dog(Animal):
#     def bark(self):
#         print("I BArk")
        
# obj = Dog()
# obj.eat()    
# obj.bark()


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Bike(Vehicle):
#     def display(self):
#         print(f"The brand of the bike is {self.brand} and the model of the bike is {self.model}")
        
# obj = Bike("Pulsar", "213")
# obj.display()    


# class Shape:
#     def info(self):
#        print("Both are generic shapes")
# class Circle(Shape):
#     pass

# class Rectangle(Shape):
#     pass

# obj = Circle()
# obj2 = Rectangle()
# obj.info()
# obj2.info()


# class Shape:
#     def info(self):
#         print("This is a generic shape.")

# class Circle(Shape):
#     pass # No modifications needed in the child class

# class Rectangle(Shape):
#     pass # No modifications needed in the child class

# # Create instances of Circle and Rectangle
# circle_instance = Circle()
# rectangle_instance = Rectangle()

# # Call the info() method on both instances
# circle_instance.info()
# rectangle_instance.info()

# class LivingBeing:
#     def breath(self):
#         print("Iam a living being and iam breathing...")

# class Animal(LivingBeing):
#     pass

# class Dog(Animal):
#     pass

# obj = Dog()
# obj.breath()        
    
# class Employee:
#     def work(self):
#         print("Both are employees")

# class manager(Employee):
#     pass

# class developer(Employee):
#     pass

# obj1 = developer()
# obj1.work()

# obj2 = manager()
# obj2.work()


class Device:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"The brand of is {self.brand}")
        
class Laptop(Device):
    pass

class Phone(Device):
    pass

class Tablet(Device):
    pass

obj = Laptop("Lenovo")
obj.display()

obj2 = Phone("Vivo")
obj2.display()

obj3 = Tablet("Samsung")
obj3.display()





