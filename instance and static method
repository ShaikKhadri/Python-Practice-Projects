
# class Bank:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#     def withdraw(self,amount):
#         self.balance-=amount
#     def display(self):
#         print("MY Name Is:",self.name)
#         print("Balance:",self.balance)
#
# a1=Bank("Khadri",1000)
# a1.deposit(1000)
# a1.withdraw(500)
# a1.display()
# class Naveen:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Naveen.count+=1
#     @classmethod
#     def total_college(cls):
#         return cls.count
# n1=Naveen("satyabama")
# n2=Naveen("mallareddy")
#
# print(Naveen.total_college())

# class students:
#     college="XYZ COLLEGE"
#     @classmethod
#     def change_college(cls,new_college):
#         cls.college=new_college
# print(students.college)
# students.change_college("KITS")
# print(students.college)

# Create a class Student that stores a student’s name, roll number, and marks.
# Create an instance method to display the student’s details and another instance method to calculate the student’s percentage.
# Create a class method to keep track of the total number of students created. Also
# create a static method that accepts marks and returns "Pass" if the marks are 40 or above, otherwise "Fail".
# Create multiple student objects and test all the methods.

class Student:
    count=0
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
        Student.count+=1
    def display(self):
        print("Nam:",self.name)
        print("ROLLNUMBER:",self.roll_number)
        print("MARKS:",self.marks)
    def percentage(self):
        return self.marks
    @classmethod
    def total_student(cls):
        return cls.count
    @staticmethod
    def check_result(marks):
        if marks>=40:
            return "PASS"
        else:
            return "Fail"
s1=Student("ROSHAN",37,98)
s2=Student("Naveen",23,88)
s3=Student("MANi",44,91)

s1.display()
print(s1.percentage())
print(Student.check_result(s1.marks))
print()
s2.display()
print(s2.percentage())
print(Student.check_result(s2.marks))
print()
s3.display()
print(s3.percentage())
print(Student.check_result(s3.marks))
print(Student.total_student())

# ⁠Create a class BankAccount that stores account holder name, account number, and balance.
# Create instance methods to deposit and withdraw money and to display the current balance.
# Create a class method to display the bank name, which is common to all accounts.
# Create a static method to check whether a withdrawal amount is valid, where the amount must be greater than zero. Create two account objects and test the methods.
class BankAccount:
    Bank_name="STATE BANK OF INDIA"
    def __init__(self,name,ano,balance):
        self.name=name
        self.ano=ano
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit:",amount)
        print("Available balance:",self.balance)
    def withdraw(self,amount):
        if BankAccount.check_money(amount):
            if amount<=self.balance:
                self.balance-=amount
            else:
                print("Insufficient funds")
        else:
            print("Invalid Funds")
        print("withdraw:",amount)
        print("Balance:",self.balance)
    def display(self):
        print("Account name:",self.name)
        print("Account number:",self.ano)
        print("Balance:", self.balance)
    @classmethod
    def display_bank(cls):
        print("Bank name:",cls.Bank_name)
    @staticmethod
    def check_money(amount):
        return amount>0
b1=BankAccount("KHADRI",445566,1000)
b2=BankAccount("ROSHAN",887766,15000)
b1.display()
b1.deposit(5000)
b1.withdraw(1000)
BankAccount.display_bank()
print(BankAccount.check_money(b1.balance))


class Appointment:
    hospital_name = "ABC Hospital"
    def __init__(self, patient_name, doctor_name, fee):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.fee = fee
    def display(self):
        print("Patient Name:", self.patient_name)
        print("Doctor Name:", self.doctor_name)
        print("Consultation Fee:", self.fee)
    def final_amount(self):
        return self.fee
    @classmethod
    def display_hospital(cls):
        print("Hospital Name:", cls.hospital_name)
    @staticmethod
    def check_fee(fee):
        return fee > 0

a1 = Appointment("Khadri", "Dr. Kumar", 500)
a2 = Appointment("Roshan", "Dr. Priya", 800)
a3 = Appointment("Rahul", "Dr. Ramesh", 0)

a1.display()
print("Final Consultation Amount:", a1.final_amount())
print()
a2.display()
print("Final Consultation Amount:", a2.final_amount())
print()
a3.display()
print("Final Consultation Amount:", a3.final_amount())
print()
Appointment.display_hospital()
print()
print("Fee Valid:", Appointment.check_fee(a1.fee))
print("Fee Valid:", Appointment.check_fee(a3.fee))




