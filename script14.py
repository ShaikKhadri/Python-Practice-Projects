from abc import abstractmethod


class Account(ABC):
    def __init__(self,balance):
        self.balance=balance
    @property
    def balance(self):
        
        return self.__balance
    @balance.setter

    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def calculate_interset(self):
        pass
class SavingAccount(Account):
    def deposit(self,amount):
        if self.validate_amount(amount):
            self.balance+=amount
            print("Amount Successfully Deposited")
        else:
            print("You have Entered invalid amount Try again!")
    def withdraw(self,amount):
        self.balance-=amount
    def calculate_interset(self):
        return 0.1* self.balance
class CurrentAccount(Account):
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def calculate_interset(self):
        return 0.01*self.balance
class FixedDeposit(Account):
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def calculate_interset(self):
        return 0.015*