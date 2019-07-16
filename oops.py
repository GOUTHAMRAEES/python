from datetime import datetime
class Employee:
    #class variable
    bonus=5000

    #parameterized contructor
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    
    def __init__(self):
        self.salary=10
    

    """
    def __str__(self):
        return self.name
    """
    #Instance non-parameterized  method
    def getSalary(self):
        return self.salary
    
    #Instance non-parameterized  method
    def applyHike(self):
        self.salary=self.salary*1.04
        return self.salary

    #Class parameterized method
    @classmethod 
    def setBonus(cls,amount):
        cls.bonus=amount

    #static methods
    @staticmethod
    def isworkingDay():
        #local variable
        day=datetime.now().strftime("%w")
        if day=='0' or day== '6':
            return False
        else:
            return True

    """
    def __repr__(self):
        return self.salary
    """
    def __add__(self,other):
        return self.salary + other.salary

class Developer(Employee):
    
    def __init__(self,stack):
        self.stack=stack
        super().__init__()
    
    def getStack(self):
        return self.stack


if __name__=='__main__':
    """
    #employee object
    emp1=Employee(1,"Goutham",20000)
    emp2=Employee(2,"Vk",25000)
    #printing emp salary
    print(emp1.salary)
    print(emp2.salary)

    #instance methods
    print(emp1.getSalary())
    print(emp1.getSalary())

#using class in the place of emp
    print(Employee.getSalary(emp1))

#class method
    Employee.setBonus(1000)
    print(emp1.bonus)

#static method
    print(Employee.isworkingDay())

#using __str__ we can print the required 
    print(emp1+emp2)
 """
    dev1=Developer("S")
    setattr(dev1,'salary',1000000)

    print(getattr(dev1,'salary'))

  
print(hasattr(dev1,'salary'))

