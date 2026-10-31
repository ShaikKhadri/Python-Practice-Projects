# FUNCTIONREFERENCE + HIGHER
# ORDER: Create a listo  lambda functions [double, triple, quadruple].Write a function apply_all(funcs, value) that applies each in sequence and returnsthefinalresult.
from functools import reduce


func=[
    lambda x:x*2,
    lambda x:x*3,
    lambda x:x*3,
]
def apply_fun(fun,value):
    for fun in func:
        value = fun(value)
    return value
result = apply_fun(func,2)
print(result)

# args + RECURSION: Write a recursive function that takes *args of numbers and
# returns their sum WITHOUT using the built-in sum()
# def recursive(*args):
#     if not args:
#         return 0
#     return args[0]+recursive(*args[1:])
# print(recursive(1,2,3,4))
# print(recursive(10,20,30))

# map() + filter() + lambda: Given a list of integers from 1 to 20, use filter() to keep
# multiples of 3, then use map() to square them. Print the result
# numbers = list(range(1,21))
# mul_of_3 = filter(lambda x:x%3==0,numbers)
# square = list(map(lambda x:x**2,mul_of_3))
# print(square)

#  PARAMETERS + LAMBDA: Write a function apply_operation(a, b, op) where op is a
# lambda. Call it with operations for add, subtract, and multiply.
# def apply_oper(a,b,op):
#     return op(a,b)
# print(apply_oper(4,5,lambda x,y:x+y))
# print(apply_oper(6,7,lambda x,y:x-y))
# print(apply_oper(2,3,lambda x,y:x*y))

#  DEFAULT + KEYWORD + LAMBDA: Write a function make_greeting(name,
# prefix='Hello', formatter=lambda x: x) that applies formatter to the final greeting string. Test
# with str.upper as the formatter.

# def make_greeting(name,prefix='hello',formatter=lambda x:x):
#     greeting = f"{prefix},{name}!"
#     return formatter(greeting)
# print(make_greeting('alice'))
# print(make_greeting("alice",formatter=str.upper))

# ALL CONCEPTS: Write a function calculator(*args, operation='add', **options) that:
# (a) uses *args to collect numbers, (b) uses a default 'add' operation, (c) supports
# operations: 'add', 'multiply', 'max', 'min' using a dict of lambda functions, (d) if options
# contains show_steps=True, prints each step of the calculation.
def calculator(*args,operation="add",**options):
    op = {
        'add': lambda x,y:x+y,
        'mul': lambda x,y:x*y,
        'max': lambda x,y:x if x>y else y,
        'min': lambda x,y:x if x<y else y,
    }
    function=op[operation]
    res=args[0]
    for i in args[1:]:
        if options.get('show_steps'):
            print(res,i,operation,":",function(res,i))
        res = function(res,i)
    return res
print(calculator(2,3,4))
print(calculator(2,3,4,operation='mul'))


# 6. Given a list of transactions where each transaction contains a type (credit or debit) and an amount,
# write a program to filter only the credit transactions, apply a 5% bonus to each transaction amount using map(),
# sort the updated transactions in descending order based on the amount, and finally compute the total credited amount using reduce().
# INPUT:
transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 500},
    {"type": "credit", "amount": 2000}
]
l=list(map(lambda x:x['amount']*1.05,filter(lambda x:x['type']=='credit',transactions)))
print(reduce(lambda x,y:x+y,sorted(l,key=lambda x:x,reverse=True)))




