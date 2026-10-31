# LEAP YEAR:   --------->  ctrl + / put the hastag
# i = int(input("enter your year:"))
# if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
#     print("leap year")
# else:
#     print("not leap year")
import functools
from functools import reduce
from unittest import result

from ARGUMENTS import update_transaction
from script7 import total_bill

# add = lambda x,y:x+y
# print(add(10,20))

# s= lambda n : n%2==0
# print(s(4))
#
# s1 = lambda x,y: x if x>y else y
# print(s1(10,5))
#
# add = lambda a,b:a+b
# mult = lambda a,b : a*b+add(a,b)
# print(mult(10,20))
# #
# # adding two list
# l =[1,2,3,4]
# l1=[5,6,7,8]
# p = list(map(lambda x,y:x+y,l,l1))
# print(p)
#
# # square (l):
# l = [1,2,3,4]
# p = list(map(lambda x:x**2,l))
# print(p)
#
# #  dividing the list of elements:
# l =[5,6,7,8]
# s = list(map(lambda x:x//2,l))
# print(s)
# #  using map and filter function
# l2 =[1,2,3,4]
# p =list(map(lambda x:x**2,l2))
# # this p also used in the filter function also
# print(list(filter(lambda x:x%2==0,p)))
#
# # an online store product price in alist write a program using map() to apply a 10% tax to each product price and dsiplay the updated price
# price=[100,200,300,400,500]
# p=list(map(lambda x:x+x*0.1,price))
# print(p)
# # A list of usernames is stored in lowercase. Use map() to format them so that the first letter is uppercase
# username=["khadri","syam","hemanth","tejs"]
# f=list(map(lambda x:x.capitalize(),username))
# print(f)
# # An e-commerce website wants to display only products priced above ₹500. Use filter() to extract those prices from a list
# price=[1000,200,300,50000,40000]
# higher_price = list(filter(lambda x:x>500,price))
# print(higher_price)
# # Write a program that uses map() to calculate the length of each word in a list of strings
# username = ["Alice","bob","henry","luffy"]
# length = list(map(lambda x:len(x),username))
# print(length)
# # - Use filter() with a lambda function to select numbers that are multiples of 4.
# l=[10,20,3,7,4,9]
# l1=list(map(lambda x:x**2,l))
# l2=list(filter(lambda x:x%4==0,list(map(lambda x:x**2,l))))
# print(l2)
#
# # Given a list of product prices, write a program to:
# #
# # * Filter prices greater than ₹500
# # * Apply a 10% discount to the filtered prices using map()
#
# price=[200,400,600,800,1000]
# l2=list(filter(lambda x:x>500,list(map(lambda x:x-x*0.1,price))))
# print(l2)
# # Given a list of integers, write a program to filter even numbers and then multiply each of them by 3 using a single pipeline.
# l=[27,12,36,98,76]
# f=list(filter(lambda x:x%2==0,list(map(lambda x:x*3,l))))
# print(f)
#
# #reduce
# import functools
# l=[1,2,3,4,7,9,14,16]
# print((reduce(lambda x,y:x+y,l)))

# sorted(iterable,key=function,reverse= )
# students=[{"name":"alice","score":85},
#           {"name":"herry","score":79},
#           {"name":"candy","score":97}]
# l=sorted(students,key=lambda x:x['score'],reverse=True)
# print(l)
#
#
# l1=["King","luffy","Prabhas","babu"]
# print(list(filter(lambda x:x[0].isupper(),l1)))

# l=[40,50]
# print(list(map(lambda x:(x*9/5)+32,l)))
# import functools
# s=[1,2,3,4,5]
# print(reduce(lambda x,y:x*y,s))
#
#
# list=["cat","elephant","dog","rhinoceros"]
# print(reduce(lambda x,y:x if len(x)>len(y) else y,list))

# l8=[100,200,300,400,600,700]
# price= list(filter(lambda x:x>500, list(map(lambda x:x-x*0.1,l8))))
# print(price)
# print(reduce(lambda x,y:x+y,price))

# def m(n):
#     if n>5:
#         return None
#     print("hi")
#     m(n+1)
# m(1)
#Write your own version of map() called my_map(func, lst) using a regular loop. Verify it
# gives the same results as the built-in.
# def my_map(fun,l):
#     result=[]
#     for i in l:
#         result.append(fun(i))
#     return result
# def square(x):
#     return x*x
# l=[10,20,30]
# print(my_map(square,l))
# print(list(map(square,l)))
# # output in the list:
# def my_map(fun,l):
#     result=[]
#     for i in l:
#         x= fun(i)
#         result.append(x)
#     return result
# def square(x):
#     return x**2
# l=[10,20,30]
# print(list(filter(lambda x:x%2==0,my_map(square,l))))

# l=["Apple","banana","cat","dog"]
# print(list(filter(lambda x:x[0].isupper(),l)))
# list = [1, 2, 3, 4, 5]
# print(reduce(lambda x,y:x*y,list))

# l5=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==1,list(map(lambda x:x*x,l5)))))

# l=[100,200,600,700,900,1000]
# p=list(filter(lambda x:x>500,list(map(lambda x:x+x*0.1,l))))
# p2=reduce(lambda x,y:x*y,p)
# print(p2)
#
# numbers = [10, -5, 20, -15, 8, -3, -12, 25]
# print(reduce(lambda x,y:x+y,list(map(lambda x:abs(x),(filter(lambda x:x<0,numbers))))))
# result=[]
# words = ["cat", "dog", "elephant", "lion", "bat", "tiger", "ox"]
#
# s=reduce(lambda x, y: x + " " + y, map(lambda x: x.upper(), filter(lambda x: len(x) > 3, words)))
# print(result)
#

# l=[1,2,3,4]
# def double(x):
#     return x**2
# result = list(map(double,l))
# print(result)
#
# result=list(map(lambda x:x**2,l))
# print(result)
#
# s=['king','lion','elephant','dluffy','roronoa zoro']
# print(list(filter(lambda x:len(x)>4,s)))
#
# print(reduce(lambda x,y:x+y,l))

# l=[200,300,600,700,800,900]
# final_bill=reduce(lambda x,y:x+y,map(lambda x:x+x*0.1,filter(lambda x:x>500,l)))
# print(final_bill)
#
# l=[2,3,4,5,-7,-9,-27,30]
# bill=reduce(lambda x,y:x+y,map(lambda x:abs(x),filter(lambda x:x<0,l)))
# print(bill)
#
# words = ["banana", "cat", "apple", "dog", "grapes", "ant"]
# result=sorted(words, key=lambda x:(len(x),x))
# print(result)
#
students = [("John", 85), ("Alice", 92), ("Bob", 85), ("David", 75)]
r=sorted(students, key=lambda x:(-x[1],x[0]))
print(r)

# 4. Given a list of integers, write a program to:
#
# * Filter numbers divisible by 2 but not by 4
# * Add 3 to each using map()
# * Sort the result in descending order
# * Find the product of all elements using reduce()

# l1=[1,2,3,4,5,6,7,12]
# result=sorted(map(lambda x:x+3,filter(lambda x:x%2==0 and x%4!=0,l1)))
# print(reduce(lambda x,y:x*y,result))
#
# words = ["Apple", "level", "Radar", "hello", "MOM", "world", "noon"]
# result=sorted(map(lambda x:x.lower(),filter(lambda x:x[0].lower()==x[-1].lower(),words)),
#               key=lambda x:(x[-1],len(x)))
# print(reduce(lambda x,y:x+" "+y,result))
#
# transactions = [
#     {"type": "credit", "amount": 1000},
#     {"type": "debit", "amount": 500},
#     {"type": "credit", "amount": 2000}
# ]
#
# caluculate_transaction=list(filter(lambda t:t['type']=='credit',transactions))
# update_transaction=list(map(lambda t:{
#     'type':t['type'],'amount':t['amount']*1.05
# },caluculate_transaction))
# sorted_transaction=sorted(update_transaction, key=lambda t:t['amount'],reverse=True)
# total_amount=reduce(lambda x,y:x+y['amount'],sorted_transaction,0)
# print(total_amount)


# def caluculate_total(*price):
#    return sum(price)
# def apply_discount(*amount):
#     total=amount[0]
#     if total > 1500:
#         return total-total*0.1/100
#     return total
# def final_bill(**details):
#     total=0
#     for key,value in details.items():
#         print(key,":",value)
#         total+=value
#     return total
# bill=final_bill(amount=apply_discount(caluculate_total(500,600,700)),tax=20,packing_charge=100)
#
# def recursive(*args):
#     if len(args) == 0:
#         return 0
#     return args[0]+recursive(*args[1:])
# print(recursive(1,2,3,4,5))
#


# func=[
#     lambda x:x*2,
#     lambda x:x*3,
#     lambda x:x*4,
# ]
# def apply_all(funcs,value):
#     for funcs in func:
#         value=funcs(value)
#     return value
# print("total:",apply_all(10,2))
# #
# def flatten(lst,depth=1):
#     result=[]
#     for item in lst:
#         if isinstance(item,list) and depth >0:
#             result.extend(flatten(item,depth-1))
#         else:
#             result.append(item)
#     return result
# print(flatten([[1,[2],3]],depth=2))


# def weighted_average(**scores):
#     total=reduce(lambda x,y:x+y,scores.values())
#     result=total/len(scores)
#     return result
# print(weighted_average(math=90,eng=85,sci=20))

#
# student=[
#     {'name':'khadri','score':90},
#     {'name':'roshan','score':85},
#     {'namae':'kaif','score':50},
# ]
# update_marks=list(filter(lambda x:x['score']>=60,student))
# add_marks=list(map(lambda x: { **x,'grade':'pass'},update_marks))
# result2=sorted(add_marks,key=lambda x:x['score'],reverse=True)
# print(result2)

# t=[
#     ('charlie',75),
#     ('naveen',80),
#     ('mani',99),
# ]
# sort_strategies = {
#     "by_name":lambda t: t[0],
#     "by_score":lambda t:t[1],
#     "by_length":lambda t:len(t[0])
# }
# for i in sort_strategies:
#     print(i)
# choice=input()
# if choice in sort_strategies:
#     sorted_student=sorted(t,key=sort_strategies[choice]
#                           )
#     print(sorted_student)
# else:
#     print("no strategy")

# def calculator(*args, operation='add', **options):
#     # Dictionary of lambda functions for operations
#     operations = {
#         "add": lambda nums: sum(nums),
#         "multiply": lambda nums:reduce(lambda x, y: x * y, nums, 1),
#         "max": lambda nums: max(nums),
#         "min": lambda nums: min(nums)
#     }
#
#     # Check if operation is valid
#     if operation not in operations:
#         return "Invalid operation"
#
#     # Show calculation steps if requested
#     if options.get("show_steps", False):
#         if operation == "add":
#             print(" + ".join(map(str, args)), "=", operations[operation](args))
#
#         elif operation == "multiply":
#             print(" * ".join(map(str, args)), "=", operations[operation](args))
#
#         elif operation in ("max", "min"):
#             print(f"{operation}({", ".join(map(str,args))}) "=",operations[operation](args)
#     return operations[operation](args)
#
#
# # Examples
# print(calculator(10, 20, 30))
# print(calculator(2, 3, 4, operation="multiply", show_steps=True))
# print(calculator(5, 8, 2, operation="max", show_steps=True))
# print(calculator(5, 8, 2, operation="min"))

