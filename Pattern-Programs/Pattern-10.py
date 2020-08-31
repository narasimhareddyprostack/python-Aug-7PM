"""
A 
B B
C C C
D D D D

Right Angle Triangle With Fixed Alphabet Symbol
#No of elements/Char in each now = i+1
#With in a row elements are repeating or not?
A - 65
B - 66
C - 67
i = 0,1,3
chr(65+i)

"""

n=int(input("Please Enter Number: "))
for i in range(n):
    print((chr(65+i)+' ')*(i+1))