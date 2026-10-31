# a = int(input())
# b = int(input())
# if a>b:
#     print("INVALID RANGE")
# else:
#     c=0
#     for i in range(a,b+1):
#         if i%11 == 0:
#             c+=1
#             print(i,end=" ")
#     if c==0:
#         print("NO NUMBERS")


# n = int(input())
# for i in range(1,n+1):
#     if(i%3==1):
#         print("A",end="")
#     elif (i%3==2):
#         print("B",end="")
#     else:
#         print("C",end="")

#
# a = int(input())
# b= int(input())
# c=0
# for i in range(a,b+1):
#     if(i%2==0):
#         c=c+1
#         if(c%2==1):
#             print(i) #--------> to find even number alternate

# a = int(input())
# b= int(input())
# c=0
# sum=0
# c1=0
# for i in range(a,b+1):
#     if(i%2==0):
#         c=c+1
#         if(c%2==1):
#             sum+=i
#             c1+=1
# print(sum/c1)

# n=int(input())
# for i in range(1,n+1):
#     if i>1:
#         print(",", end="")
#     if i%2==1:
#         print("A", end="")
#     else:
#         print("B", end="")


# n = int(input("Enter n: "))
#
# for i in range(1, n + 1):
#     if i > 1:
#         print(",", end="")
#
#     if i % 2 == 1:
#         print("A", end="")
#     else:
#         print("B", end=

# n=int(input())
# for i in range(1,n+1):
#     if i>1:
#         print(",",end="")
#     if i%3==1:
#         print("A",end="")
#     elif i%3==2:
#         print("B",end="")
#     else:
#         print("C",end="")


 # https://talkpu.sh/t/nnCNc1S8n

# def discount_price(price,discount=10):
#     return price - (price*discount/100)
# print(discount_price(200))

n=int(input())
if n<=0:
    print("INVALID INPUT")
else:
    c=0
    num=2
    while(c<n):
        fc=True
        for i in range(2,int(num**0.5)+1):
            if n%i==0:
                fc=False
                break
            if fc:
                c+=1
            if c>1:
                print(end=",")
            print(i,end="")
        num+=1


