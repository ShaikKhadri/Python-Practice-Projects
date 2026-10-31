# Design a payment system using method overriding and polymorphism.
# Create a base class Payment with a method pay(double amount).
# Create subclasses CreditCard, UPI, and NetBanking that override the pay() method to implement their own payment logic.
# Demonstrate runtime polymorphism by calling pay() on a Payment reference pointing to different subclass objects.
class Payment:
    def __init__(self,amount):
        self.amount=amount
    def process(self):
        print("Process Payment")
class Creditcard(Payment):
    def process(self):
        print("Credit class:",self.amount)
class Upi(Payment):
    def process(self):
        print("UPI Payment Process:",self.amount)
class NetBanking(Payment):
    def process(self):
        print("Net banking is:",self.amount)
def checkout(payment):
    payment.process()
p1=Creditcard(5000)
p2=Upi(7000)
p3=NetBanking(8000)
checkout(p1)
checkout(p2)
checkout(p3)



