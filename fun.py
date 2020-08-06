'''
x=eval(input("Enter value:"))
print(type(x))


x = eval("10+20+40.7")
print(x, type(x))



from sys import argv
print(type(argv))   # list type <class 'list'> 

print(argv[1])

print(argv)


from sys import argv
print("The no of cmd line arguments :", len(argv))
print("The list of command line arguments:", argv)
print("The command line arguments one by one:") 
for x in argv:
	print(x) 



from sys import argv
args = argv[1:]
print(args)
sum = 0
for x in args:
    sum =sum+int(x)
print("sum", sum)


from sys import argv
print(int(argv[1]) + int(argv[2]))
print(int(argv[1]) + int(argv[2]))



a,b,c = 1,2,3
print("Values are :", a,b,c, sep="a")

name="narasimha"
salary="20000"
employeer="IBM"

print('Hello {0}, your Salar is {1} and your company {2} @ Bangalore'.
       format(name,salary, employeer))

       
print('Hello {0}, your Salar is {1} and your company {1} @ Bangalore'.
       format(name,salary, employeer))

print('Hello {0}, your Salar is {1} and your company {2} @ Bangalore'.
       format(name,salary, employeer))

       
print('Hello {a}, your Salar is {b} and your company {c} @ Bangalore'.
       format(a=name,b=salary, c=employeer))



a=10

print('a is %i' %a)


name="narasimha"
marks=[10,20,30]
print("Hello %s, and your marks are: %s"   %(name, marks))




price = 70.56789
print('price value = {}'.format(price))
print('Price value = %f' %price)

price = 70.56789
print('price value = {}'.format(price))
print('Price value = %.2f' %price)




a =20
print(type(a))
print(id(a))

'''



