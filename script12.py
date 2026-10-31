import numbers
from logging.config import stopListening
from pydoc import text


# class A:
#     def __init__(self):
#         self.value=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value<=5:
#             num=self.value
#             self.value+=1
#             return num
#         else:
#             raise StopIteration
# obj = A()
# for i in obj:
#     print(i)

# if we dont use for loop then
# l=[1,2,3,4]
# it=iter(l)
# print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())

#generator

# def m1(start,stop):
#     while start<=stop:
#         yield start
#         start+=1
# x=m1(5,10)
# print(next(x))
# print(next(x))
# print(next(x))


# class F:
#     def __init__(self,n):
#         self.n=n
#         self.count=0
#         self.current=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#        if self.count<self.n:
#            num=self.current
#            self.current+=2
#            self.count += 1
#            return num
#        raise StopIteration
# n=int(input("Enter your number:"))
# obj1=F(n)
# for i in obj1:
#     print(i)

# class String:
#     def __init__(self,text):
#         self.text=text
#         self.index=len(text)-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index>=0:
#             value=self.text[self.index]
#             self.index-=1
#             return value
#         raise StopIteration
# text=input("Enter your String:")
# o=String(text)
# for ch in o:
#     print(ch)

class Odd:
    def __init__(self,number):
        self.number= number
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.number):
            v=self.number[self.index]
            self.index+=1
            if v%2!=0:
                return v
        raise StopIteration
number=[12,13,14,6,7,5,37]
a=Odd(number)
for i in a:
    print(i)

def m1():
    yield


