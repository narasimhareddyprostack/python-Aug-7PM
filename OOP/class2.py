class emp_Data:
    '''Employee Data'''
    def __init__(self,name,age):
        self.name = name 
        self.age = age
   
    def emp_Details(self):
        print("Employee Name", self.name)
        print("Employee Age", self.age)


emp = emp_Data('Narasimha Reddy', 37)
emp.emp_Details()

emp2 = emp_Data('Raj', 38)

emp2.emp_Details()


#this, current obj - JAva, Javascript
#self in python - current object