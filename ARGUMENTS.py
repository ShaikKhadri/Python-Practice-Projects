# Design a Python program for a supermarket billing system. Create a function calculate_total(*prices) that accepts the
# prices of multiple items and returns their total cost. Then define a function apply_discount(*amount) that applies a (10% discount)
# if the total exceeds 1500. Finally, create a function final_bill(**details) that accepts keyword arguments such as amount, tax, and packing_charge,
# and returns the final payable bill. Display the final amount using a single nested function call.
from functools import reduce

from pip._internal.operations import prepare

from script4 import transactions


# def caluculate_total(*prices):
#     total=0
#     for i in prices:
#         total*=i
#     return total
# def apply_discount(*amount):
#     total=sum(amount)
#     if total >1500:
#         total=total-total*10/100
#     return total
# def final_bill(**details):
#     total=0
#     for key,value in details.items():
#         print(key,":",value)
#         total+=value
#     return total
# print(final_bill(amount=apply_discount(caluculate_total(100,200,400)),tax=200,packing_charge=200))
# Write a function order_food(*items, **preferences)
# that accepts multiple food items and optional preferences like spice level or delivery time. Display the order summary
# def order_food(*items,**preferences):
#     print("FOOD ITEMS:")
#     print(f"{items}")
#     if preferences:
#         print("\npreference")
#         for key,value in preferences.items():
#             print(key,":",value)
# order_food('PIZAA','BURGER','CHICKEN 65',spicy_level=200,medium_level=100,high_level=400)
# Create a function student_info(name, *subjects, **details) that prints a student’s name,
# subjects enrolled, and additional details like grade and school.
# def student_info(name,*subjects,**details):
#     print("Students name:",name)
#     print("Students enrolled:")
#     for i in subjects:
#         print(i)
#     for key,value in details.items():
#         print(key,":",value)
# student_info('KHADRI','Python','HTML','Java',School="patricks high school",Grade="A")
# Write a function shopping_cart(discount=0, *prices) that calculates the total price
# after applying a discount. Demonstrate calling the function with and without the discount argument.
# def shopping_cart(*prices,discount=0):
#     total=0
#     for i in prices:
#         total+=i
#     final_price=total-total*discount/100
#     print("Total:",total)
#     print("Discount:",discount,"%")
#     print("FINAL:",final_price)
# shopping_cart(100,200,300)
# shopping_cart(100,200,300,discount=20)
# Design a function register_user(username, role="user", *permissions, **details)
# that stores user information, including optional permissions and additional attributes.
# def register_user(username, role="user", *permissions, **details):
#     print("Username:",username)
#     print("role:",role)
#     print("\npermissions:")
#     for i in permissions:
#         print(i)
#     print("Additional details:")
#     for key,value in details.items():
#         print(key,":",value)
# register_user('khadri','read','WRITE','music',email='skroshan26@gmail.com',department='it')
# import copy
# users = [
#     {"name": "Khadri", "age": 22},
#     {"name": "Rahul", "age": 25}
# ]
# shallow_copy=copy.copy(users)
# deep_copy=copy.deepcopy(users)
# users[1]["age"]=45
# print(shallow_copy)
# print(deep_copy)
# Write a function calculate_score(base_score=0, *bonus_points, **penalties)
# that computes a final score after adding bonuses and subtracting penalties.
def caluculate_score(base_score=0,*bonus_Points,**penalties):
    print("Bonus points:")
    final_score=base_score
    for i in bonus_Points:
        final_score+=i
    for key,value in penalties.items():
        final_score-=value
        print("base score:",base_score)
        print("Bonus points:",bonus_Points)
        print("penalyties:",penalties)
        print("final_score:",final_score)
caluculate_score(100,20,25,40,late_submission=15,wrong_submission=30)

def create_html_tag(tag, **attributes):
    html = "<" + tag
    for key, value in attributes.items():
        html += f" {key}='{value}'"
    html += ">"
    print(html)
# Function call
create_html_tag(
    'a',
    href='https://python.org',
    target='_blank'
)
# 6. Given a list of transactions where each transaction contains a type (credit or debit) and an amount, write a program to filter only the credit transactions, apply a 5% bonus to each transaction amount using map(), sort the updated transactions in descending order based on the amount, and finally compute the total credited amount using reduce().
# INPUT:
transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 500},
    {"type": "credit", "amount": 2000}
]
credit_transaction=list(filter(lambda t: t['type'] == "credit",transactions))
apply_transaction=list(map(lambda t:{'type':t['type'],'amount':t['amount']*1.05},credit_transaction))
update_transaction=sorted(apply_transaction, key=lambda t:t['amount'],reverse=True)
final_transaction=reduce(lambda x,y:x+y['amount'],update_transaction,0)
print("final transaction:",final_transaction)




