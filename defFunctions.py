#   Write a function power(base, exponent) that returns base raised to exponent using the
# ** operator.
# def power(base,exponent):
#     return base ** exponent
# print(power(2,3))

  # Create a function full_name(first, middle, last) that returns the full name as a single  string.
# def full_name(first,middle,last):
#     return first+" "+middle+" "+last
# print(full_name("monkey","D","luffy"))

#  Write a function intro(name, city, hobby) that prints a sentence about a person. Call it
# in two different orders and observe the difference
# def intro(name,city,hobby):
#     print("My name is:",name,"my location  is:",city,"my hobby is",hobby)
# intro("Khadri","Cricket","hyd") ------>n the first call, the arguments are in the correct order, so the sentence makes sense.
# In the second call, the arguments are passed in a different order, so the values are assigned to the wrong parameters, producing a meaningless sentence.

 # Write a function discount_price(price, discount=10) that returns the discounted price. Test with and without the discount argument.
# def fiscount_price(price,discount=10):
#     discounted = price-price*discount/100
#     return discounted
# print(fiscount_price(100))
#
# def details(**kwargs):
#     total=0
#     for key,value in kwargs.items():
#         print(key,":",value)
# details(name="khadri",city="guntur",age=22)

# def multiply(*args):
#     total=1
#     for i in args:
#         total*=i
#     return total
# print(multiply(1,2,3,4))

def person(name,*hobbies):
    print("my name is:",name)
    print("hobbies:",hobbies)
person("khadri","cricket","music","movies")

def fun(*args):
    print(type(args))
fun(1,2,3)

# Write a function create_html_tag(tag, **attributes) that prints: <tag key='val' ...>.
# Example: create_html_tag('a', href='https://python.org', target='_blank')
def html_tag(tag,**attribute):
    html = "<"+tag
    for key,value in attribute.items():
        html += f" {key}='{value}'"
    html += ">"
    print(html)
html_tag("a", href='https://python.org', target='_blank')

