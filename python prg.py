# 1.Write a program to convert kg to g. (Input 5.6kg print in grams)
# n = float(input("enter the number:"))
# gms = n*1000
# print(n,"weight in grms:",gms)
import operator

# Write a program to covert temperature from degree C to F. (Input 80C)
# n=float(input("enter the number:"))
# fahrenheit = (n*9/5) + 32
# print(f"{fahrenheit:.2f}F")

# 3.Declare and initialize 3 three variable and print the biggest number.
# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# c = int(input("enter the number:"))
# if(a>b and a>c):
#     print("the biggest number is:",a)
# elif(b>c):
#     print("the biggest number is:",b)
# else:
#     print("the biggest number is:",c)

# 4.Write a  program that performs the following tasks.
# a.Store a number in a variable
#a = int(input())
#b.If value is not in range (100-1000) prints wrong number else follows the steps
# if(a>=100 and a<=100):
#     if(a%2==0):
#         print(a%3)
#     else:
#         print(a%2)
# else:
#     print("wrong number")
# c.Check even or odd
# d.If even divide the number by 3 and print the remainder
# e.If odd divide the number by 2 and print the remainder.

#6.Write a program to perform simple math based on the user inputs by using Switch condition.(+ , - , * , /)
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = input()
# if(c=='+'):
#     print(a+b)
# elif(c=='-'):
#     print(a-b)
# elif(c=='*'):
#     print(a*b)
# elif(c=='/'):
#     print(a/b)
# else:
#     print("invalid input")

#7.Write a program to print CVCORP for 33 times.
# n=int(input("enter a number"))
# if(n>=11 and n<=99):
#     for i in range(1,n+1):
#         print("CV CORP")
# else:
#     print("invalid input")

# 8.Write a program to print all numbers which are divisible by 11 from 250 to 550.
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# for i in range(a,b+1):
#     if(i%11==0):
#         print(i)

# 9.Write a program to sum all the numbers from 56 to 153.
# sum=0
# c=0
# for i in range(56,153):
#     sum+=i
#     c=c+1
# avg = sum/c
# print(f"{avg:2f}")

# 10.Write a program to print all even numbers in range 700 to 900.
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# for i in range(a,b+1):
#     if(i%2!=0):
#         print(i)

# write a program to find even numbers using arthmetic
# operator in the arthemetic operator % operatornot used use remaning order
#using division
# n=int(input())
# if (n//2)*2==n:
#     print("even number is:",n)
# else:
#     print("not an even number")
#using *:
# n=int(input())
# if int(n*0.5)*2==n:
#     print("even number is:",n)
# else:
#     print("not an even number")
# using subtract:
n=int(input())
while n>1:
    n=n-2
if n==0:
    print("even number")
else:
    print("odd number")
# using additon:
n=int(input())
x=0
while x<n:
    x=x+2
if x==n:
    print("even number")
else:
    print("odd number")