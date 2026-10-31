#
# balance = 10000
# def deposit(amount):
#     global balance
#     balance+= amount
#     return balance
#
#
# def withdraw(amount):
#     global balance
#     if amount<= balance:
#         balance -= amount
#         return "withdraw successful"
#     else:
#         return "insufficient balance"
# print(deposit(100))
# print(withdraw(12200))
#
#
#
#
# a=int(input())
# b=int(input())
# c=0
# if a>b:
#     for i in range(a,b-1,-1):
#         c+=1
#         if c>1:
#             print(end=", ")
#         if i<0:
#             print(f"{5}*({i})",end="")
#         else:
#             print(f"{5}*{i}",end="")
# else:
#     for i in range(a,b+1):
#         c+=1
#         if c>1:
#             print(end=", ")
#         if i<0:
#             print(f"{5}*({i})",end="")
#         else:
#             print(f"{5}")

a=int(input())
b=int(input())
sum=0
c=0
if a>b:
    print("INVALID RANGE")
else:
    for i in range(a+1,b):
        if i%2==0:
            sum+=i
            c+=1
    if c==0:
        print("NO NUMBERS")
    else:
        print(sum)
