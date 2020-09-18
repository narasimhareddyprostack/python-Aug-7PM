def fact(n):
    if n==1:
        return n
    else:
       return n* fact(n-1)

print(fact(5))


'''
5 * fact(4) 24

4 *  fact(3) 6

3 * fact(2) 2
2 * fact(1) 1
1* 1
'''