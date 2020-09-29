
class Emp:
    '''Emp class ( Desc) '''
    cname = ' IBM'
    def __init__(self,eno1,ename2,esal3):
        print('Object Created...') 
        self.eno = eno1
        self.ename = ename2
        self.esal = esal3

    def info(self):
        a  = 100
        print('Employee No:', self.eno)
        print('Employee Name:', self.ename)

    @classmethod    
    def getCompanyName(cls):
        print('Company Name:', cls.cname)

    


e1=Emp(101, 'Narasimha Reddy', 500000)
e1.info()
e1.getCompanyName()
e1.wish()




