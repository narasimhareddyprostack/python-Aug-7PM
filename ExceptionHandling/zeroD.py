print('Good Morning')
try:
    print(10.5/0)  
except ZeroDivisionError as x:
    print(x)
except ValueError as v:
    print(v)
except FloatingPointError as f:
    print(f)
except Exception as e:
    print("Exception",e)
finally:
    print('Good After Noon')
