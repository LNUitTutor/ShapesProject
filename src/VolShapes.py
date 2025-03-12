from abc import ABC, abstractmethod
from FlatShapes import *

class Shape3D(ABC):
    def __init__(self, shape, number):
        self.base = shape
        self.height = number
    def Volume(self):
        return self.base.area() * self.height
    def LateralArea(self):
        return self.base.perim() * self.height
    def BaseArea(self):
        return self.base.area()
    def TotalArea(self):
        return 2*self.BaseArea() + self.LateralArea()
    def __gt__(self,other):
        return self.Volume() > other.Volume()
    @abstractmethod
    def __str__(self):
        pass

class Cylinder(Shape3D):
    def __init__(self, radius = 1, height = 1):
        Shape3D.__init__(self, Circle(radius), height)
    def __str__(self):
        return f'Cylinder[r = {self.base.r}, h = {self.height}]'
        
class Parallelepiped(Shape3D):
    def __init__(self, a = 3, b = 4, c = 5):
        Shape3D.__init__(self, Rectangle(a, b), c)
    def __str__(self):
        return f'Parallelepiped[{self.base.a} x {self.base.b} x {self.height}]'


if __name__ == '__main__':
    a = Cylinder()
    b = Cylinder(5, 8)
    print(a)
    print('v =', a.Volume(),'  s =', a.TotalArea())
    print(b)
    print('v =', b.Volume(),'  s =', b.TotalArea())
    if a>b:
        print("max =",a)
    else:
        print("max =",b)
    c = Parallelepiped()
    d = Parallelepiped(3, 3, 3)
    print(c)
    print('v =', c.Volume(),'  s =', c.TotalArea())
    print(d)
    print('v =', d.Volume(),'  s =', d.TotalArea())
        
    
