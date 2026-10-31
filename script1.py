# create a python application to design a function for food delivery application where customers
# name as a positional argument the order type is default argument the function where the order type
# is regular the function should accept multiple food items ordered by the customer using positional
# arguments and additional details such as address ,payment mode,delivery instruction using keyword
# arguments the function should display the complete order summary including customer
# details list of items ordered total no of items at all additional information

# def swiggy(customer_name,order_type="regular",*items,**customer_details):
#     print("hi",customer_name)
#     print("order type is:",order_type)
#     print("your cart:")
#     total_bill=0
#     for item in items:
#         print(item[0],":Rs",item[1])
#         total_bill+=item[1]
#     print("total item in the cart:",len(items))
#     print("total bill is Rs:",total_bill)
#     print("additional details:")
#     for detail,about in customer_details.items():
#         print(detail,":",about)

# swiggy("gowtham","swiggy one",
#        ["burger",265],["fries" ,60],["coke", 40],
#        payment_mode = "upi",delivery_instrution = " dont ring the bell",cutlery= "yes provide cultery")

# print(type(swiggy))
# zomato = swiggy
# zomato("name","zomat gold",["biriyani",100],["gulabjam",50],payment_mode="upi")

  # user define function    reference function
# def square(a):
#     return a*a
# def cube(a):
#     return a**3
# def double(fun,value):
#     return fun(fun(value))
# print(double(square,10))
# print(double(cube,2))


# def fun(a,b):
#     print("the value of a:",a)
#     print("the value of b:",b)
# fun(6,7)

def greet():
    print("hi")

say_hlo=greet
print(say_hlo())

def outer():
    def inner():
        print("hello")
    func=inner
    func()
outer()

def fun():
    def fun2():
