a = 50
b = a
print( a == b) #True

print (a is b)  # True

print("******")

list1 = [1,2,3,"four"]
list2 = [1,2,3,"four"]

print(list1 == list2)  # True
print(list1 is not list2)  # False

# when you have to compare content ,use ==

# when you have to compare object ref , use is

"""
a = 5

str1= " Hello"

list1 = [1,2,"three"]

set = { 1,2,3,1,2,3}

tuple1 = (1,2,3)
#Json , Dict
"""
