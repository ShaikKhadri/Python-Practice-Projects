def multi(a,b,c):
    return a*b*c
print(multi(1,2,3))


def describe_pet(animal,name):
    print("my", animal, "is", name)
describe_pet(animal="animal",name="dog")


def add(a,b):
    return a+b
add (10,20)


## TypeError: add() missing 1 required positional argument: 'b'

def power(base,exponent):
    return base ** exponent
print(power(3,2))

def full_name(first,middle,last):
    return first+" "+middle+" "+last+" "
print(full_name("monkey","d","luffy"))


