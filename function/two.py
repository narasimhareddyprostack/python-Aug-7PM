emp1 = [100,200,300,400]
emp2 = [100,100,100,100]
emp3 = [1,2,3,4]


def f1(a):
    total= 0
    for x in a:
        total = total+x
    return total

print(f1(emp1))
print(f1(emp2))
print(f1(emp3))
