class Student:
    def __init__(self,name,age,marks,subject):
        self.name=name
        self.age=age
        self.marks=marks
        self.subject=subject
    def __str__(self):
        return f"Student name is {self.name} has gotten marks{self.marks}"
    def __repr__(self):
        return f"students({self.name},{self.age},{self.marks},{self.subject})"
    def __len__(self):
        return len(self.name)
    def __contains__(self, item):
        return item in self.subject
    def __add__(self, other):
        return self.age+other.age
    def __sub__(self, other):
        return self.age-other.age
    def __mul__(self, other):
        return self.age*other.age
    def __truediv__(self, other):
        return len(self.subject)/len(other.subject)
    def __floordiv__(self, other):
        return len(self.subject)//len(other.subject)
    def __mod__(self, other):
        return len(self.subject)%len(other.subject)
    def __lt__(self, other):
        return self.marks<other.marks
    def __gt__(self, other):
        return self.marks>self.marks
    def __eq__(self, other):
        return self.marks==other.marks
    def __ne__(self, other):
        return self.marks!=other.marks
    def __le__(self, other):
        return self.marks<=other.marks
    def __ge__(self, other):
        return self.marks>=other.marks
    def __hash__(self):
        return self.age
obj1 = Student("Alice", 27, 78, ['Maths', 'Science'])
obj2 = Student("Reene", 22, 79, ['Maths', 'Science', 'Geography', 'Civics'])
obj3 = Student("Meg", 25, 72, ['Maths'])
obj4 = Student("Candice", 24, 98, ['Maths', 'Civics', 'Science'])
obj5 = Student("Max", 23, 88, ['English', 'Python'])
print(obj1)
print(str(obj1))
print(repr(obj2))
print(len(obj1))
print(obj1+obj2)
print(obj2-obj1)
print(obj2*obj3)
print(obj1/obj3)
print(obj3//obj1)
print(obj2%obj4)
print(hash(obj4))


# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __add__(self, other):
#         return self.price+other.price
# p1=Product("APPLE",1500)
# p2=Product("VIVO",700)
# print(p1+p2)
