n=int(input("Please Enter Some Number"))
c = 1
for i in range(n):
    for j in range(i+1):
	    print(c, end=' ')
	    c=c+1
    print()