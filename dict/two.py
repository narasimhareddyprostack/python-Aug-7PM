d = { }
print(type(d))

d = { "s_Name":"Narasimha", "s_Age":37}
print(d)
# accessing
print(d['s_Name'])

print(d['s_Age'])

for x in d:
    print("Key :" ,x, "value:", d[x])


list = [10,20,30]
for x in list:
    print(x)