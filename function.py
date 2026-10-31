# def m1(x):
#     print(x)
# m1(10)
#
#
# def m2():
#     print("hi class!")
#     return 10
# m2()   #---------> 1st function call khali hi class print hota
# print(m2()) #------. 2n call print pura hota and return type bhi hota return ni hai to none output Aata
#
from email.mime.multipart import MIMEMultipart


# keyword argument
# def learn(name,skill):
#     print("my name is:",name,"im learning",skill)
# learn(name="KHADRI",skill="SQL")



# write a python programm to build a simple uber application that has a function called trip details with parameters like driver name,pick up location,drop location,total price
# now called this function using positional arguments and keyword arguments

# def trip_details(name,pickuplocation,droplocation,totalprize):
#     print("your driver name is:",name)
#     print("from:",pickuplocation)
#     print("to:",droplocation)
#     print("fare:",totalprize)
# print(trip_details(name="khadri",totalprize=120,pickuplocation="kphb",droplocation="hitech"))
# print(trip_details("KHADRI","kphb","Hitech city","120"))
#


# def send_email(to,subject,body):
#     print("the emaol is:")
#     return  to,subject,body
# print(send_email(to ="khadri",body="text",subject="ai"))
# print(send_email("khadri","ai","text"))

# Deposit function
# def deposit(amount):
#     if amount>0:
#         return "account deposited" +  amount
#     else:
#         return "insufficient balance"
# # Withdraw function
# def withdraw(amount):
#     return "Amount Withdrawn: " + str(amount)
#
# # Check Balance function
# def check_balance():
#     return "Current Balance: 1000"
# print(deposit(500)); print(withdraw(300)); print(check_balance())


def fun(age,name="user",city ="hyderabad"):
    print("hello!:",name)
    print("your city:",city)
    if age>18:
        print("you are eligible for vote")
    else:
        print("you are not eligible for vote")
fun(20)


def multiply(*args):
   product =1
   for i in args:
       product = product*i
       print(product)
multiply(6,5,2)


# create apython apliaction to develop a simple hospital billing system design function like calculate wll with positional aguements charges of variable or orbitary type and another function install insurance with keyword arguements of variable or orbitary
# create another fun add taxes with keyword arg of varible or orbitary length the program should accept multiple choices like consultation,.... apply insurance reduction and add tax

# def caluculate_bill(*charge):
#     return sum(charge)
#
# def app_insurance(amount,**insurance):
#     total_claim = 0
#     print("INsurance details:")
#     for key, value in insurance.items():
#         print(key,":",value)
#         total_claim += value
#     return total_claim
#
# def caluculate_taxes(amount,**taxes):
#     total_tax = 0
#     print("TAX details:")
#     for key, value in taxes.items():
#         print(key,":",value)
#         total_tax += value
#     return total_tax
# print("Final Hospital Bill =",caluculate_taxes(app_insurance(caluculate_bill(1500,200,2000),LIC=1000, store=4500),gst=180, gst2=50))
#
#
#

# total_bill = caluculate_bill(1500,2000,20000)
# total_bill = app_insurance(total_bill,"LIC"=1000,"store"=4500)
# total_bill = caluculate_taxes(total_bill,"GST"=100,"GST"=200)


# Create a function that accepts the prices of any number of products and returns the total price.
# Create another function that accepts the total amount and calculates 18% GST.
# Create a function that accepts keyword arguments such as amount, gst, and delivery_charge, and displays each bill detail using a for loop before returning the final bill.
# Display the final payable amount using a single nested function call. 

def product(*args):
    return sum(args)
def p2(amount):
    if amount>1800:
        amount= amount+(amount*0.05)
    return amount
def p3(amount,**insurance):
    total =amount
    for key, value in insurance.items():
        print(key,":", value)
        total = total+value
    return total
print("Final bill:",p3(amount=p2(product(100,900,900)),salary=100,bonus=1000,hra=200))


