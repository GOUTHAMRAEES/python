class A:
    def __init__(self):
        self.__price=100
    
    def getPrice(self):
        return self.__price
    
    def setPrice(self,price):
        self.__price=price

class B(A):
    pass
a=B()
print(a.getPrice())
a.setPrice(10)
print(a.getPrice())
a.__price