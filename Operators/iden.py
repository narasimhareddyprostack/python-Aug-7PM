a = "5"
b = a
print(id(a))
print(id(b))
c = 6
print(id(c))

print("*********")
list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1
print(id(list1))
print(id(list2))
print(id(list3))
