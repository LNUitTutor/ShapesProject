from abc import ABC, abstractmethod
from math import sqrt
from FlatShapes import *

class Shape3D(ABC):
    def __init__(self, shape, number):
        self.base = shape
        self.height = number
    @abstractmethod
    def Volume(self):
        pass
    @abstractmethod
    def LateralArea(self):
        pass
    def BaseArea(self):
        return self.base.area()
    @abstractmethod
    def TotalArea(self):
        pass
    def __gt__(self,other):
        return self.Volume() > other.Volume()
    @abstractmethod
    def __str__(self):
        pass

class DirectShape(Shape3D):
    def Volume(self):
        return self.base.area() * self.height
    def LateralArea(self):
        return self.base.perim() * self.height
    def TotalArea(self):
        return 2*self.BaseArea() + self.LateralArea()

class Cylinder(DirectShape):
    def __init__(self, radius = 1, height = 1):
        Shape3D.__init__(self, Circle(radius), height)
    def __str__(self):
        return f'Cylinder[r = {self.base.r}, h = {self.height}]'
    def __repr__(self):
        return f'Cylinder({self.base.r}, {self.height})'
        
class Parallelepiped(DirectShape):
    def __init__(self, a = 3, b = 4, c = 5):
        Shape3D.__init__(self, Rectangle(a, b), c)
    def __str__(self):
        return f'Parallelepiped[{self.base.a} x {self.base.b} x {self.height}]'
    def __repr__(self):
        return f'Parallelepiped({self.base.a}, {self.base.b}, {self.height})'

class TriangularPrism(DirectShape):
    def __init__(self, side1 = 3, side2 = 3, angle = 60, h = 5):
        Shape3D.__init__(self, Triangle(side1, side2, angle), h)
    def __str__(self):
        return f'TriangularPrism[base = {self.base}, h = {self.height}]'

class ConicalShape(Shape3D):
    def Volume(self):
        return self.base.area() * self.height / 3
    def TotalArea(self):
        return self.BaseArea() + self.LateralArea()

class Cone(ConicalShape):
    def __init__(self, radius = 1, height = 1):
        Shape3D.__init__(self, Circle(radius), height)
    def __str__(self):
        return f'Cone/r = {self.base.r}, h = {self.height}\\'
    def __repr__(self):
        return f'Cone({self.base.r}, {self.height})'
    def LateralArea(self):
        L = sqrt(self.base.r ** 2 + self.height ** 2)
        return 0.5 * self.base.perim() * L

class RectangularPyramid(ConicalShape):
    def __init__(self, a = 3, b = 4, height = 1):
        Shape3D.__init__(self, Rectangle(a, b), height)
    def __str__(self):
        return f'Rectangular Pyramid/base = {self.base}, h = {self.height}\\'
    def LateralArea(self):
        Ha = sqrt((self.base.b*0.5) ** 2 + self.height ** 2)
        Hb = sqrt((self.base.a*0.5) ** 2 + self.height ** 2)
        return self.base.a * Ha + self.base.b * Hb

class TriangularPyramid(ConicalShape):
    def __init__(self, side1 = 3, side2 = 3, angle = 60, height = 1):
        Shape3D.__init__(self, Triangle(side1, side2, angle), height)
    def __str__(self):
        return f'Triangular Pyramid/base = {self.base}, h = {self.height}\\'
    def LateralArea(self):
        r = self.base.area() * 2 / self.base.perim()
        apopheme = sqrt(r ** 2 + self.height ** 2)
        return 0.5 * self.base.perim() * apopheme


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
    e = TriangularPrism()
    f = TriangularPrism(5, 12, 90, 13.5)
    print(e)
    print('v =', e.Volume(),'  s =', e.TotalArea())
    print(f)
    print('v =', f.Volume(),'  s =', f.TotalArea())
    g = Cone()
    print(g)
    h = RectangularPyramid()
    print(h)
    i = TriangularPyramid()
    print(i)
    L = {a, b, c, d, e, f, g, h, i}
    print('Largest shape is', max(L))
    print('Total surface is', sum(s.TotalArea() for s in L))

        
    
