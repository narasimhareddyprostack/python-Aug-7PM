
def f1():
    global a
    a = 20
    print(a)  # a is local declaration is, value 20

def f2():
    print(a)  # 10


b = 20

f1()
f2()
print(a+b)

# recursive function
# filter
# map
# OOP

