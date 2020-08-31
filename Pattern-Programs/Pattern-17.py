n=int(input("Please Enter Number: "))
for i in range(n):
    for j in range(n-i):
        print(n-j, end=' ')
    print()