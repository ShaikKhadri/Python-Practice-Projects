# FUNCTION REFERENCE
def apply_fun(fun,value):
    return fun(value)
def square(x):
    return x*x
def double(x):
    return x*2
print(apply_fun(square,5,))
print(apply_fun(double,3))

# Assign the built-in function len to a variable called count. Use it to find the length of a list
count= len
list=[10,20,30,40,50,60]
print(count(list))

# Write a function run_twice(func, value) that calls func on value twice and returns the
# final result.

def run_twice(func,value):
    result=func(value)
    result=func(result)
    return result
def add_one(x):
    return x*2
print(run_twice(add_one,4))

l=[(1,'banana'),(2,'apple'),(3,'cherry')]
print(sorted(l,key=lambda x:x[(1)]))