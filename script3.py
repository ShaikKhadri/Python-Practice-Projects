def grek(prize,quantity):
    totalcost = prize * quantity
    deliverycost = 40
    if totalcost<200:
        return totalcost+deliverycost
print(grek(40,3))



def add(sum1,sum2,sum3):
    return sum1+sum2+sum3

def avg(sum1,sum2,sum3):
    return sum1+sum2+sum3/3

def display(add,avg):
    print(add(2,3,5))
    print(avg(2,3,5))

