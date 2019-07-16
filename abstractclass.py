from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

class Circle(Shape):
    def getArea(self):
        return 1*3*5

circle=Circle()
print(circle.getArea())
