# num=[4,5,6,7]
# it =iter(num)
# print(it.__next__())
# print(next(it))
# class Top10:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=10:
#             val=self.num
#             self.num+=1
#             return val
#         else:
#             raise StopIteration
# value=Top10()
# for i in value:
#     print(i)
from os import lstat


# class Number:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n%2==0 and self.n<=10:
#             val=self.n
#             self.n+=1
#             return val
#         else:
#             raise StopIteration
#
# n=int(input())
# obj=Number(n)
# for i in obj:
#     print(i)

class Positive:
    def __init__(self,lst):
        self.lst=lst
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.i < len(self.lst):
                val=self.lst[self.i]
                self.i+=1
                if val>0:
                    return val
        raise StopIteration
lst=list(map(int,input().split( )))
a=Positive(lst)
for s in a:
    print(s,end=" ")