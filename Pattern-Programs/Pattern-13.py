"""
A
A B
A B C
A B C D

# With in row, number/symbols are changing. We must have to use inner/nested loop.
No of elements in each row = i+1
A - 65 
B - 66 
C - 67 
chr(65+i)
"""
n=int(input("Please Enter Number: "))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end=' ')
    print()