# class Bank:
#     bank_year="HDFC BANK"
#     def __init__(self,accountholder_name,acc_number,balance,pin):
#         self.accountholder_name=accountholder_name
#         self.acc_number=acc_number
#         self.balance=balance
#         self.pin=pin
# alice=Bank("ALICE",1234567,7890,2627)
# print(alice.accountholder_name)
# print(alice.acc_number)


# class Bank:
#     bank_year = "HDFC BANK"
#     def __init__(self,balance):
#         self.__balance=balance
#     @property
#     def balance(self):
#         user=input("Enter username:")
#         pin=int(input("Enter your pin:"))
#         if user=="admin" and pin==2222:
#             return self.__balance
#         else:
#             return "Access Denied"
# alice=Bank(10000)
# print(alice.balance)

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#         self.count=3
#     @property
#     def balance(self):
#             pin=int(input("Enter pin:"))
#             if pin==1234:
#                 self.count=3
#                 return self.__balance
#             else:
#                 self.count-=1
#                 return f"Access Denied you made a unsuccessful attempt.{self.count}"
#     @balance.setter
#     def balance(self,value):
#         if value>0:
#             self.__balance=value
#         return "Invalid"
#     def deposit(self,amount):
#         self.__balance+=amount
#     def withdraw(self,amount):
#         self.__balance-=amount
# account=BankAccount(1000)
# print(account.balance)
# account.deposit(5000)
# print(account.balance)
# account.withdraw(3000)
# print(account.balance)
# import math
#
# class Circle:
#     def __init__(self,radius):
#         self.__radius=radius
#     @property
#     def radius(self):
#         return self.__radius
#     @radius.setter
#     def radius(self,new_radius):
#         if new_radius>0:
#             self.__radius=new_radius
#     @property
#     def area(self):
#         return math.pi * self.__radius**2
#     @property
#     def circumference(self):
#         return 2*math.pi * self.__radius
# c1=Circle(5)
# print(c1.radius)
# print(c1.area)
# print(c1.circumference)

class Config:
    def __init__(self):
        self.system_name="SWS"
        self.setting={"theme":"dark",
                      "language":"English"}
        self._secret_key="ABC123"
        self.__secret_key="XYZ789"
    def get_setting(self,key):
        return self.setting.get(key)
c1=Config()
print(c1.setting)
print(c1._secret_key)
print(c1._Config__secret_key)
print(c1.get_setting("language"))