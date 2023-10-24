import math
class Circle:
    def __init__(self,r):
        self.radius = r
        
    def area(self) -> float:
        return math.pi*self.radius*self.radius
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    

c = Circle(2)
print(c.area())
print(c.perimeter()) 
    