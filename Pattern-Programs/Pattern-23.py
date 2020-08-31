"""
While print some patterns in python, we need to write some formulas.
TO get the pattern we need formula

Step 1: We need to find out the common factor

1
2   7
3   8   12
4   9   13  16
5   10  14  17  19
6   11  15  18  20  21


row = 0 and value = 1 (row+1)
row = 1 and value = 2 (row+1)
common factor's 
7-2, 8-3, 9-4 ....  : diff is 4,3,2,1
val = val +dec 
dec = dec-1



"""
n = int(input("Please Enter Number of Row: "))
for i in range(n):
    val = i+1
    dec = n-1
    for j in range(i+1):
        print(format(chr(64+val), "<3"), end=' ')
        val = val+dec
        dec = dec-1
    print()