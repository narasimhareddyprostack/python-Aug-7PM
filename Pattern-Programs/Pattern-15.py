"""
	0 1 2 3 4
	* * * * *
	*	    *  
	*	    *
	*	    *
	* * * * *
    Logic : i == 0 or j ==0 or i==n-1 or j==n-1
    No of elements : i == 0 or j ==0 or i==n-1 or j==n-1
    No of space , else

# The outer print is used to print the ‘*’ and the inner print is used to print the blank spaces.
#We are printing the * only if i == 0 , i == length – 1, j == 0 or j == length – 1. i.e.
# we are printing symbol for the first row, last row, first column and last column. 
# For other values, we are printing blank spaces.
"""
n=int(input("Please Enter Number: "))
for i in range(n):
    for j in range(n):
        if( i == 0 or j ==0 or i==n-1 or j==n-1):
            print('*', end=' ')
        else:
            print('&', end=' ')
    print()