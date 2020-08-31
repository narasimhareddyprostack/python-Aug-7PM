"""
D C B A
D C B
D C
D

D - 68 (64 + n -j)
B - 67 
C - 66
A - 65
"""

n=int(input("Please Enter Number: "))
for i in range(n):
    for j in range(n-i):
        print(chr(64+n-j),end=' ')
    print()