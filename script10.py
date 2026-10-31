class Bank:
    def __init__(self,ano,apin,self_balance):
        self.ano=ano
        self.apin=apin
        self.self_balance=self_balance
    def deposit(self,amount):
        if amount>0:
            self.self_balance+=amount
            print(f"the account xxxxxx{self.ano%1000}has been credit your amount:",amount)
    def withdraw(self,amount):
        if amount<0:
            print("Invalid amount")
        elif amount > self.self_balance:
            print("Insufficient funds")
        else:
            self.self_balance-=amount
            print(f"Your account xxxxxx{self.ano %1000}has been debit with amount:",amount)
    def check_balance(self):
        print("Your current balance is:",self.self_balance)
ac1 = Bank(1234563892,4444,100000)
ac2 = Bank(2345678456,9999,1500)
ano = int(input("Enter your accountno:"))
if ano==ac1.ano:
    pin = int(input("enter your pin:"))
    if pin == ac1.apin:
        print("Login successful")
        while True:
            print("1.Deposit\n2.Withdraw\n3.checkbalance")
            choice=int(input("enter your choice:"))
            if choice==1:
                amount=int(input("Enter your deposit amount:"))
                ac1.deposit(amount)
            elif choice==2:
                amount=int(input("Enter the amount you want to withdraw:"))
                ac1.withdraw(amount)
            elif choice==3:
                ac1.check_balance()
            else:
                print("Invalid Choice")
                break
    else:
        print("Invalid pin")
elif ano==ac2.ano:
    pin = int(input("enter your pin:"))
    if pin == ac2.apin:
        print("Login successful")
        while True:
            print("1.Deposit\n2.Withdraw\n3.checkbalance")
            choice=int(input("enter your choice:"))
            if choice==1:
                amount=int(input("Enter your deposit amount:"))
                ac2.deposit(amount)
            elif choice==2:
                amount=int(input("Enter the amount you want to withdraw:"))
                ac2.withdraw(amount)
            elif choice==3:
                ac2.check_balance()
            else:
                print("Invalid Choice")
                break
    else:
        print("Invalid pin")
else:
    print("Invalid account number")

