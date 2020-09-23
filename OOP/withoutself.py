class Test:
    a = 10
    print("Hello",id(a))
    def wish():
        print('inside Wish()')
    
    def __init__(self):
        print('First Init Method')

    def __init__(self):
        print('second Init Method')
    
obj = Test()
print(obj.a)

print('*' * 10)
print(id(obj))
