# us=0
# username="luffy"
# password="luffy@1234"
# def login(username,password):
#     global us
#     if username=="luffy" and password=="luffy@1234":
#         us=us+1
#         print("login sucessfull")
#         return True
#     else:
#         print("invalid username or password")
#         return False
# for i in range(3):
#     user=input("enter the username")
#     pwd=input("enter the password")
#     if login(user,pwd):
#         break
# else:
#     print("Account is locked")

# Decorators Questions create functions add(a, b), subtract(a, b) and multiply(a, b).
# Create a function calculate(operation, a, b) that accepts a function reference and performs the selected operation.
# Use lambda functions to perform:
# Square of a number
# Cube of a number
# Double of a number Add a decorator log_operation that prints "Operation started" before execution and "Operation completed" after execution.

def log_operation(func):
    def wrapper(*args):
        print("Operation started")
        res=func(*args)
        print("Operation completed")
        return res
    return wrapper
@log_operation
def add(a,b):
    return a+b
@log_operation
def sub(a,b):
    return a-b
@log_operation
def mul(a,b):
    return a*b

def calculate(op,a,b):
    return op(a,b)

square=lambda x:x**2
cube=lambda x:x**3
double=lambda x:x*2

print("Addition:",calculate(add,10,5))
print("Subtraction:",calculate(sub,10,5))
print("Multiplication:",calculate(mul,5,10))

print("square:",square(2))
print("cube:",cube(3))
print("double:",double(5))

# A system wants to track the number of times the login() function is
# called. Create a global variable attempts = 0 and a decorator track_attempts
# that increments the global variable every time the login function is executed.
# The login() function should accept username and password as parameters and display "Login attempted by <username>".
# Call the function three times with different usernames and passwords,
# and finally display the total number of login attempts.
# Use the global keyword inside the decorator to modify the global variable
# attempts = 0
# def decorator(func):
#     def wrapper(username,password):
#         global attempts
#         attempts+=1
#         return func(username,password)
#     return wrapper
# @decorator
# def login(username,password):
#     print("Login attempted by:",username)
#
# login('khadri',1234)
# login("roshan",2345)
# login("mani",3456)
#
# print("Total login attempted:",attempts)

# An ATM system has a function withdraw(username, pin, amount).
# Create a decorator authenticate that checks whether the username is "admin" and PIN is "1234".
# If authentication is successful, execute the function; otherwise, display "Invalid credentials".
# The function should maintain a global balance = 10000, deduct the amount
# if sufficient balance exists, and display the remaining balance.
balance = 1000
def authenticate(func):
    def wrapper(username,pin,amount):
        if username=="admin" and pin=="1234":
            return func(username,pin,amount)
        else:
            print("Invalid creditantial")
    return wrapper
@authenticate
def login(username,pin,amount):

    if amount<=balance:
        print("Remaining balance:",balance)
    else:
        print("Insufficent balance")
login("admin","1234",200)
login("admin","14",300)
login("admin","1234",400)

