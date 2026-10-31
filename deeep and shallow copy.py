# org_msg = [['hi',],['how are you?']]
# import copy
# shal_cpy = copy.copy(org_msg)
# shal_cpy[0] = ['hey']
# print(shal_cpy)
#
#
# org_msg = [['hi','hlo khadri'],['how are you?']]
# import copy
# deep_cpy = copy.deepcopy(org_msg)
# deep_cpy[0][0] = ['hey']
# print("original messege:", org_msg)
# print("deep copy:", deep_cpy)

# def final_amount(amount,discount_amount):
#     return amount-discount_amount
# print(final_amount(discount_amount=400,amount=700))

# Design a Python program for a supermarket billing system. Create a function calculate_total(*prices)
# that accepts the prices of multiple items and returns their total cost. Then define a function
# apply_discount(*amount) that applies a 10% discount if the total exceeds 1500. Finally,
# create a function final_bill(**details) that accepts keyword arguments such as amount, tax, and
# packing_charge, and returns the final payable bill. Display the final amount using a single nested function call.

# def caluculate_total(*prices):
#     total= 0
#     for price in prices:
#         total += price
#     return total
# def apply_discount(*amount):
#     total = amount[0]
#     if total>1500:
#         return total - (total*0.1)
#     return total
# def final_bill(**details):
#     total =0
#     for services, charge in details.items():
#         print(services,":",charge)
#         total+= charge
#     print("your final bill is $",total)
# item1 = int(input("enter your first item: "))
# item2 = int(input("enter your second item: "))
# item3 = int(input("enter your third item: "))
# total = caluculate_total(item1,item2,item3)
# total = apply_discount(total,item1,item2)
# final_bill(amount=total,packing_charge=200,shipping_charge=100)



