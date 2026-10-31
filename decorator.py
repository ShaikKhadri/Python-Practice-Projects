from arbitary import caluculate_total


# def my_decorator(func):
#     def wrapper():
#         print("HELLO ")
#         func()
#         print("OREWA D LUFFY")
#     return wrapper
# @my_decorator
# def greet():
#     print("iam")
# greet()

from logging import exception


# Create a function place_order(item)
#     Write a decorator that prints:
#     * “Function started” before execution
#     * “Function ended” after execution

# def my_decorator(func):
#     def wrapper(item):
#         print("Before started")
#         func(item)
#         print("After started")
#     return wrapper
# @my_decorator
# def place_order(item):
#     print(f"order placed is {item}")
# place_order('laptop')
# Create a function greet(name) Write a decorator that adds:
# * “Welcome!” before
# * “Have a nice day!” after
# def my_decorator(func):
#     def wrapper(name):
#         print("Welcome!")
#         func(name)
#         print("Have a nice day!")
#     return wrapper
# @my_decorator
# def greet(name):
#     print(f"My Name is{name}")
# greet("KHADRI")
# Create a function transfer_money()
#     Write a decorator that prints:
#     * “Transaction started”
#     * “Transaction successful” / “Transaction failed”
# def transfer_decorator(func):
#     def wrapper():
#         print("Transaction started")
#     try:
#         func()
#         print("Transaction Successful")
#     except:
#         print("Transaction failed")
# @transfer_decorator
# def transfer_money():
#     print("Money transferred")
#     raise Exception("Insufficent balance")
# Create a function start_system() Write a decorator that prints: * “System starting…” before execution * “System started successfully” after execution
# def system_decorator(func):
#     def wrapper():
#         print("Systen Starting....")
#         func()
#         print("System Started Successfully")
#     return wrapper
# @system_decorator
# def start_system():
#     print("System is  running")
# start_system()
# Create a function get_message() that returns "hello user". Write a decorator using @ syntax that converts the output to uppercase.
# def upper_decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
# @upper_decorator
# def upper():
#     return ("hello khadri")
# print(upper())
# # Create a function get_number() that returns 10 Use a decorator to return double the value.
# def number_decorator(func):
#     def wrapper():
#         return func() * 2
#     return wrapper
# @number_decorator
# def get_number():
#     return 10
# print(get_number())
# Create a function add(a, b) Use a decorator to print:
#     * “Calculating sum…”
#     * “Calculation done”
# def add_decorator(func):
#     def wrapper(a,b):
#         print("Caluculating Sum...")
#         result = func(a,b)
#         print("caluculating done")
#         return result
#     return wrapper
# @add_decorator
# def add(a,b):
#     return a + b
# print(add(5,5))

# def price_decorator(func):
#     def wrapper(price):
#         print("Apply discount")
#         result = func(price)
#         print("Discount applied")
#         return result
#     return wrapper
# @price_decorator
# def apply_discount(price):
#     return price * 0.90
# print(apply_discount(100))

# def verif_user(func):
#     def wrapper(*args,**kwargs):
#         print("user verified")
#         func(*args,**kwargs)
#     return wrapper
# def user_verified(func):
#     def wrapper(*args,**kwargs):
#         print("Transaction logged")
#         func(*args,**kwargs)
#     return wrapper
# #they are 2 methods:
# #1
# @verif_user
# @user_verified
# def check_balance():
#     print("balance displayed")
# check_balance()
#2
# def check_balance():
#     print("Balance displayed")
# check_balance=user_verified(verif_user(check_balance))
# check_balance()

# def bold(func):
#     def wrapper(*args,**kwargs):
#         return "**"+func(*args,**kwargs)+"**"
#     return wrapper
# def italic(func):
#     def wrapper(*args,**kwargs):
#         return "_"+func(*args,**kwargs)+"_"
#     return wrapper
# @bold
# @italic
# def msg(item):
#     return f"HELLO! {item}"
# print(msg("Khadri"))

# from functools import wraps
# def decorator(func):
#     @wraps(func)
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper
# @decorator
# def greet():
#     """The Function Prints Hello"""
#     print("Hello!")
# greet()
# print(greet.__name__)
# print(greet.__doc__)

# class Enrollment:
#     platform="LearnOnline"
#     enrollment_count=0
#     def __init__(self,name,course,age):
#         self.name=name
#         self.course=course
#         self.age=age
#         if self.age >= 18:
#             self.status="Registered"
#             Enrollment.enrollment_count+=1
#         else:
#             self.status="Rejected"
# e1=Enrollment("Khadri","Python",19)
# e2=Enrollment("Roshan","Java",17)
# e3=Enrollment("Mani","Sql",20)
#
# print("PLatform:",Enrollment.platform)
# print(e1.name,e1.status)
# print(e2.name,e2.status)
# print(e3.name,e3.status)
#
# print(isinstance(e1,Enrollment))
# print(isinstance(e2,Enrollment))
# print(isinstance(e3,Enrollment))

# def log_operation(func):
#     def wrapper(*args):
#         print("Operation Started")
#         result=func(*args)
#         print("Operation ended")
#         return result
#     return wrapper
# @log_operation
# def add(a,b):
#     return a+b
# @log_operation
# def sub(a,b):
#     return a-b
# @log_operation
# def mul(a,b):
#     return a*b
#
# def calculate(operation,a,b):
#     return operation(a,b)
#
# print(calculate(add,10,5))
# print(calculate(sub,10,5))
# print(calculate(mul,10,5))
#
# square = lambda n:n*n
# cube = lambda n:n*n*n
# double = lambda n:n*2
#
# print("Square:",square(5))
# print("cube:",cube(5))
# print("Double:",double(5))

def processing(func):
    def wrapper(*args):
        print("Before executed")
        result=func(*args)
        print("after executed")
        return result
    return wrapper
@processing
def process_marks(marks,opeartion):
    result=[]
    for mark in marks:
        result.append(opeartion(mark))
    return result
marks=[30,40,50,60,80]
grace=lambda mark:mark+5
double=lambda mark:mark*2
greater=lambda mark:mark>40
print("Grace marks:",process_marks(marks,grace))
print("Double marks:",process_marks(marks,double))
print("Greater:",process_marks(marks,greater))

balance = 10000
def authenticate(func):
    def wrapper(username, pin, amount):
        if username == "admin" and pin == "1234":
            func(username, pin, amount)
        else:
            print("Invalid credentials")

    return wrapper
@authenticate
def withdraw(username, pin, amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
withdraw("admin", "1234", 3000)
withdraw("user", "1234", 2000)
withdraw("admin", "1234", 4000)

attempts = 0


def login_required(func):
    def wrapper(username, password, exam_name):
        if username == "student" and password == "1234":
            func(username, password, exam_name)
        else:
            print("Invalid credentials")
    return wrapper
def track_attempt(func):
    def wrapper(username, password, exam_name):
        global attempts
        attempts += 1
        func(username, password, exam_name)
    return wrapper
@track_attempt
@login_required
def start_exam(username, password, exam_name):
    print("Exam started for", username)
    print("Exam name:", exam_name)
start_exam("student", "1234", "Python")
start_exam("student", "1234", "SQL")
start_exam("student", "1234", "HTML")
print("Total exam attempts:", attempts)



