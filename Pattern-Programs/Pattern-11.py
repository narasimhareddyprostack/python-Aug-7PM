"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

#No of digits in each row: i+1

"""
n=int(input("Please Enter Number: "))
for i in range(n):
    print((str(i+1)+' ')* (i+1))