# def employe(details_name,salary,bonus):
#     total = salary+bonus
#     print("employee name:",details_name)
#     print("salary:",salary)
#     print("bonus:",bonus)
#     print("total:",total)
# employe("khadri",20000,100)
import keyword


#            ARBITARY ARGUMENTS
# Every customer buys a different number of items.
#
# Customer 1 buys 2 items.
# Customer 2 buys 5 items.
# Customer 3 buys 10 items.
#
# You don't know in advance how many item prices will be passed.

# Design a Python program for a supermarket billing system. Create a function calculate_total(*prices)
# that accepts the prices of multiple items and returns their total cost. Then define a function
# apply_discount(*amount) that applies a 10% discount if the total exceeds 1500. Finally, create a function
# final_bill(**details) that accepts keyword arguments such as amount, tax, and packing_charge, and
# returns the final payable bill. Display the final amount using a single nested function call.


def caluculate_total(*price):
    return sum(price)

def caluculate_discount(*amount):
    total = amount[0]
    if total > 1500:
        total = total -(total * 0.10)
    return total

# def final_bill(**details):
#     amount = details["amount"]
#     tax = details["tax"]
#     package = details["package"]
#     return amount+tax+package
#
# bill = final_bill(amount=caluculate_discount(caluculate_total(500,600,700)),tax=100,package = 50)
# print(bill)
# using for loop in keyword arguments
def final_bill(**details):
    total = 0
    for key,value in details.items():
        print(key,":",value)
        total += value
        return total
print("bill:",final_bill(amount=caluculate_discount(caluculate_total(500,600,700)),tax = 100,package = 50))