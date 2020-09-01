a = [10,20]

a[0] = 100
print(a)

b = [10,20,30]

b.insert(0,100)
b.insert(1,200)

print(b)


# List :  group of values as single entity ,==  [10,20,"thirty", 10]

# duplicate allowed
# insertion order preserved,  
# hetro/dis similar  [10,10.5,"thirty"]
# mutable   a[0] = "ten"

# dynamic   a.append()/a.insert(1,20)