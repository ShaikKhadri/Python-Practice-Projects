# # Generator that yields numbers from 1 to N
# def number(n):
#     for i in range(1,n+1):
#         yield i
# n=int(input("enter:"))
# n1=number(n)
# for i in n1:
#     print(i)
# # Generator that yields even numbers from 1 to N
# def even(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i
# n=int(input("Enetr:"))
# n1=even(n)
# for i in n1:
#     print(i)
# # Generator that yields each character of a string
# def characters(text):
#     for ch in text:
#         yield ch
# text = input("Enter string: ")
# for ch in characters(text):
#     print(ch)
#
# def reverse(text):
#     for i in range(len(text)-1,-1,-1):
#         yield text[i]
# text=input("Enter string:")
# t=reverse(text)
# for ch in t:
#     print(ch)
# # Generator for cumulative sum
# def cumulative(number):
#     total=0
#     for i in number:
#         total+=i
#         yield total
# number=[1,2,3,4]
# for i in cumulative(number):
#     print(i)
#
# # create a class A that has two class and instance variable create a class B that is the child class of A which has one instance and one class variable access all these properties using an object of b

def vowels(n):
    while n<=10:
        sq=n*n
        yield sq
        n+=1
n=int(input())
a=vowels(n)
for i in a:
    print(i)

def char(s):
    for ch in s:
        if ch.lower() in "aeiou":
            yield ch
s=input()
c=char(s)
for a in c:
    print(a)
