# single inheritance
# class A:
#     c1= "hey"
#     c2 = 786
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# class B(A):
#     c3 = True
#     def __init__(self,z,x,y):
#         self.z=z
#         super().__init__(x,y)
# b=B(10,20,30)
# print(b.c1)
# print(b.c2)
# print(b.c3)
# print("z:",b.z)
# print("Y:",b.y)
# print("X:",b.x)
# # multiple inheritance
# class A:
#     def __init__(self,x):
#         self.x=x
# class B(A):
#     def __init__(self,x,y):
#         self.y=y
#         super().__init__(x)
# class C(B):
#     def __init__(self,x,y,z):
#         self.z=z
#         super().__init__(x,y)
#
# b=C(10,20,30)
# print("Z:",b.z)
# print("X:",b.x)
# print("Y:",b.y)
class A:
    def _init_(self):
        print("A Constructor!!")

class B(A):
    def _init_(self):
        print("B Constructor!!")
        super()._init_()
class C(B):
    def _init_(self):
        print("C Constructor!!")
        super()._init_()
c = C()
print(C.mro())
print(B.mro())
print(A.mro())
# Multiple inheritance
class A:
    def __init__(self):
        print("A Constructor")
        super().__init__()
class B:
    def __init__(self):
        print("B Constructor")
class C(A,B):
    def __init__(self):
        print("C Constructor")
        super().__init__()
a1=C()
print(A.mro())
print(B.mro())
print(C.mro())
#
# # Hierarchical Inheritance
class A:
    def __init__(self):
        print("A Constructor")
class B(A):
    def __init__(self):
        print("B Constructor")
        super().__init__()
class C(A):
    def __init__(self):
        print("C Constructor")
        super().__init__()
c=C()
b=B()
print(C.mro())
print(B.mro())
# # hybrid inheritance means hierachical and multi level
class A:
    def __init__(self):
        print("A Constructor!!")
class B(A):
    def __init__(self):
        print("B Constructor!!")
        super().__init__()
class C(A):
    def __init__(self):
        print("C Constructor!!")
        super().__init__()
class D(B, C):
    def __init__(self):
        print("D Constructor!!")
        super().__init__()
d=D()
print(D.mro())
for a in D.mro():
    print(a.__name__)
# class A:
#     def __init__(self):
#         print("A constructor")
#     def m1(self):
#         print("mid m1")
#     @classmethod
#     def m2(cls):
#         print("class method is A")
# class B(A):
#     def __init__(self):
#         print("B Constructor")
#         super().__init__()
#     def m1(self):
#         print("Mid 2")
#     @classmethod
#     def m2(cls):
#         print("Class method is B")
#         super().m2()
# class C(B):
#     def __init__(self):
#         print("C Constructor")
#         super().__init__()
#     def m1(self):
#         print("Mid c")
#     @classmethod
#     def m2(cls):
#         print("Class method is c")
#         super().m2()
# c=C()
# C.m2()

# class A:
#     def __init__(self):
#         self.x=10
#         self.y=20
#         self.z=30
#         self.count=40
#     def check_even(self,value):
#         if value%2==0:
#             print("Even")
#         else:
#             print("Odd")
# class B:
#     def __init__(self,count):
#         self.count=count
#     def m1(self):
#         obj=A()
#         obj.check_even(self.count)
# b=B(100)
# print(b.count)
# b.m1()
# print(b.count)

# create an Employee class with:
# • emp_name
# • salary
# • display_details()
# Create a Manager class that inherits Employee and adds a bonus(). Display the
# total salary.

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display_details(self):
#         print("Employee name:",{self.name},"employee salary:",{self.salary})
# class Manager(Employee):
#     def bonus(self):
#         self.salary+=self.salary*0.1
# alice=Manager("Alice",15000)
# alice.display_details()
# alice.bonus()
# alice.display_details()

# Class 1: Restaurant
# # • Create a method menu(item) that returns the price of the selected food
# # item.
# # Class 2: FoodCourt (inherits Restaurant)
# # Create the following methods:
# # • display_menu() – Display the available food items.
# # • order() – Accept the food item from the user and allow multiple orders.
# # • billing() – Display the total bill and add a packing charge of ₹20.
# # Class 3: Customer (inherits FoodCourt)
# # • Create an object of the Customer class.
# # • Call the order() method.
# class Restaurant:
#     def __init__(self,item):
#         items={
#             "burger":200,
#             "Pizza":300,
#             "coke":70,
#             "fries":90
#         }
#         return items.get(item)
# class FoodCourt(Restaurant):
#     def display_menu(self):
#         print("burger-->200\nPizza-->300\nCoke-->70fries--->90")
#     def biiling(self,total_cost):
#         print("Your Total_cost:",total_cost)
#         print("Packaging charge:RS20")
#         print("Your total is:",total_cost+20)
#     def order(self):
#         total_cost=0
#         while(True):
#             self.display_menu()
#             item=input("Enter your Order name :")
#             price=self.menu(item)
#             if price is not None:
#                 total_cost+=price
#             else:
#                 print("Invalid item")
#             choice=input("DO you want to  add more order?y/n")
#             if choice=="n":
#                 break
#         self.billing(total_cost)
# class Customer(FoodCourt):
#     pass
# o1=Customer()
# o1.order()

# Class 1: Cab
# • Create methods to calculate the fare for Bike, Auto, and Car rides.
# Class 2: Uber (inherits Cab)
# • Create the methods menu(), booking(), and billing().
# • Add 10% GST and apply a 15% discount if the bill is above ₹1000.
# Class 3: Ola (inherits Cab)
# • Create the methods menu(), booking(), and billing().
# • Add 12% GST and apply a 20% discount if the bill is above ₹1500.
# Driver Code
# • Ask the user to choose Uber or Ola and call the booking() method.
# class Cab:
#     def bike(self,distance):
#         return distance*300
#     def Auto(self,distance):
#         return distance*350
#     def Car(self,distance):
#         return distance*500
# class Ola(Cab):
#     def menu(self):
#         print("Bike-->300KM\nAuto-->350KM\nCar-->500KM")
#     def billing(self,cost):
#         cost=cost+cost*0.12
#         if cost>1500:
#             cost=cost-cost*0.12
#         print("Your total fare:",cost)
#     def booking(self):
#         self.menu()
