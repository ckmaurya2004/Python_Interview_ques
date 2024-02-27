from abc import ABCMeta,ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea():
        return 

class Square(Shape):
    def __init__(self,length):
        self.length = length

    def printArea(self):
        return self.length*self.length
    

sq = Square(5)
print(sq.printArea())

