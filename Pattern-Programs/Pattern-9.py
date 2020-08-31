
"""
* * * * *
* * * *
* * *
* *
*

No of stars in each row = n-i
Note: With in row has no element are not changing, then nested or inner loop not required
"""
n=int(input("Please Enter Number: "))
for i in range(n):
    print('* '* (n-i))  