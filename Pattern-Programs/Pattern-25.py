"""
1
2 7 
3 6 8
4 5 9 10
"""

num=int(input("Please Enter Number of rows: "))
for i in range(num):
    for j in range(i+1):
        x = 0
        for k in range(j):
            x = x+num-k
        if j %2== 0:
            print(chr(64+x+i-j+1), end=' ')
        else:
            print(chr(64+x+num-i),end=' ')
    print()        
