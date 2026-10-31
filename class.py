# class Phone:
#     s="Android"
#     c=0
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#         Phone.c+=1
# s1 = Phone("Samsung",1000)
# print(Phone.c)
#



# class User:
#     def __init__(self,age):
#         self.age=age
#         print("Object created")
# age=int(input("Enter age:"))
# if age>=18:
#     user1=User(age)
# else:
#     print("No obeject creation")


# class BankAccount:
#     bank_name="ABC Bank"
#     def __init__(self,account_holder,account_number,balance):
#         self.account_holder=account_holder
#         self.account_number=account_number
#         if balance<0:
#             self.balance=0
#         else:
#             self.balance=balance
#     def display_details(self):
#         print("Bank Name:",BankAccount.bank_name)
#         print("Account holder:",self.account_holder)
#         print("Account number:",self.account_number)
#         print("Balance:",self.balance)
# s1=BankAccount("Khadri",12234,1000)
# s2=BankAccount("Syam",23455,-23)
# s1.display_details()
# s2.display_details()
# A college wants to maintain student records. Create a class Student
# with a class variable college = "ABC College" and instance variables name, roll_no, and marks.
# Initialize these values using __init__(). The constructor should validate that marks are between 0 and 100;
# if invalid marks are provided, set them to 0. Create three student objects and display their details.

# class Student:
#     college="ABC College"
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         if marks < 0 or marks > 100:
#             self.marks=0
#         else:
#             self.marks=marks
#     def display_details(self):
#         print("College name:",Student.college)
#         print("Student name;",self.name)
#         print("Roll no:",self.roll_no)
#         print("Marks:",self.marks)
# a1=Student("KHADR",41,786)
# a3=Student("Luffy",79,89)
# a1.display_details()
# a3.display_details()
# An online store wants to maintain a list of products added to its system.
# Create a global list products = []. Create a class Product with a class variable store_name = "ABC Store"
# and instance variables name, price, and quantity. Initialize the values using the constructor and validate that price and
# quantity cannot be negative. Whenever a product object is created, add its name to the global products list.
# Create three products and display the product details and the complete product list.
# list_product=[]
# class Product:
#     store_name="ABC Store"
#     def __init__(self,name,price,quantity):
#         self.name=name
#         if price > 0 and quantity > 0:
#             self.price=price
#             self.quantity=quantity
#         else:
#             self.price=0
#             self.quantity=0
#     def display(self):
#         print("Product:",Product.store_name)
#         print("Product name:",self.name)
#         print("Product price:",self.price)
#         print("Quantity:",self.quantity)
#         list_product.append(self.name)
# c1=Product('Laptop',1000,2)
# c2=Product('headphones',2000,3)
# c3=Product('phone',1500,5)
# c1.display()
# c2.display()
# c3.display()
# print("Complete product:",list_product)


# class A:
#     x=20
#     def __init__(self,y):
#         self.y=y
# o1=A("Hello")
# o2=A("hii")
# o3=A("Yo")
# A.x=40
# print(A.__dict__)
# print('Data in o1')
# print(o2.x)

class Employee:
    company = "Tech corp"
    employee_count=0
    def __init__(self,name, department, salary,experience):
        if salary <0:
            salary=0
        if experience<0:
            experience=0
        Employee.employee_count+=1
        self.Employee_id= "EMP"+str(Employee.employee_count)
        self.name=name
        self.department=department
        self.salary=salary
        self.experience=experience
        if experience>5:
            bonus_percentage=15
        if experience>=3:
            bonus_percentage=10
        else:
            bonus_percentage=5
        bonus = salary*bonus_percentage/100
        final_salary=bonus+salary
        self.pay_details ={
            "name": name,
            "salary": salary,
            "experience": experience,
            "bonus": bonus,
            "final_salary": final_salary
        }
e1=Employee('khadri','AI',50000,7)
e2=Employee('mani','cse',20000,8)
e3=Employee('shiva','it',10000,6)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)

class zomato:
    discount=0.2
    coupon_code="py20"
    res_name=[]
    res_no=0
    def __init__(self,res_name,res_menu):
        self.res_name=res_name
        zomato.res_no+=1
        self.res_menu=res_menu
        self.res_id=zomato.res_no
paradise=zomato("paradise",{"Chicken Biryani":200,
                            "Mutton":400,
                            "coke":40})
Pista_House= zomato("Pista House",
                  {"Chicken Biryani" : 250,
                   "Mutton Biryani" : 290,
                   "Apricot Delight" : 200})
KFC = zomato("KFC",
                  {"Chicken Burger" : 200,
                   "Chicken Wings" : 350,
                   "Coke" : 40,
                   "Fries" : 70})
def order(item_no,restaurant):
    order_item=list(restaurant.res_menu.items())
    cost=order_item[item_no-1][1]
    print("Your cart value is:",cost)
    print("Do You have coupon code?")
    cc =input("Y/N?")
    if cc=="Y":
        code=input("enter your coupon code:")
        if code==zomato.coupon_code:
            cost = cost-cost*zomato.discount
        else:
            print("Invalid Coupon code")
    print("Your Final Bill is :Rs",cost)
c=0
for i in zomato.res_name:
    c+=1
    print(c,":",i)

choice = int(input("enter your resturant number:"))
if choice ==1:
    c=0
    for i in paradise.res_menu.items():
        c+=1
        print(c,":",i)
    item_no=int(input("enter your item number:"))
    order(item_no,paradise)
elif choice ==2:
    c=0
    for i in Pista_House.res_menu.items():
        c+=1
        print(c,":",i)
    item_no=int(input("enter your item number:"))
    order(item_no,Pista_House)
elif choice == 3:
    c = 0
    for i in KFC.res_menu.items():
        c += 1
        print(c, ":", i)
    item_no = int(input("enter your item number:"))
    order(item_no, KFC)
else:
    print("Invalid Input")