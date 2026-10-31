def greet(name,age,grade):
    print(f"hello,{name},my age is: {20},grade:{grade}")
greet("Teja",'20','A')
# the
# function
# send_email(to, subject, body)
# using
# keyword
# arguments in any
# # order.

def send_email(to,subject,body):
    print(f"to :{to},subject is:{subject},body:{body}")
send_email(subject='sick leave',body='fever',to='prathima')

# create apython apliaction to develop a simple hospital billing system design function like calculate wll with
#     positional aguements charges of variable or orbitary type and another function install insurance with keyword arguements of variable or orbitary
# # create another fun add taxes with keyword arg of varible or orbitary length the program should accept
# # multiple choices like consultation,.... apply insurance reduction and add tax
def hos_bill(*args):
     total_bill=0
     for i in args:
         total_bill+=i
     return total_bill
def insurance(amount,**kwargs):
    total_claim=0
    for key,values in kwargs.items():
        print(f"{key}:{values}")
        total_claim+=values
        return total_claim
def tot_bill(amount,**kwargs):
    total_tax=0
    for key,values in kwargs.items():
        print(f"{key}:{values}")
        total_tax+=values
        return amount-total_tax
total_bill=(hos_bill(100,2000,3000))
print(total_bill)
total_claim=insurance(tot_bill,lic1=100,lic2=300,lic3=800)
print(total_claim)


