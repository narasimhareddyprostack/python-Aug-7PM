i=0
def order():
    global i
    i+=1
    print('Order Successfully created',i)
    order()
    
order()

#disadvatages
#1.recursion logic, might be hard to understand
#2.debugging problemm
#3.lot memory and time.
