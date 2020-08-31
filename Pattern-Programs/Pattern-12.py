"""
1
1 2
1 2 3
1 2 3 4

# With in row, number/symbols are changing. We must have to use inner/nested loop.
No of elements in each row = i+1

"""
n=int(input("Please Enter Number: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end=' ')
    print()