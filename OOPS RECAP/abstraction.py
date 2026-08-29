## Abstraction is process of hiding the implementation details from the user.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

# concrete class
class Rectangle(Shape):
    def __init__(self,length:int,width:int):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)

r=Rectangle(10,20)
r.area()