a = 10
def display():
    a = 20
    global c
    c = 30
    print(a)   #  20

def display1():
    b = 20
    print(a)  # 10
    print(b)  # 20
    print(c)  # 30



display()
display1()

