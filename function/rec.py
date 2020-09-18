i=0
def order():
    global i
    i+=1
    print('Order Successfully created',i)
    order()
    
order()
