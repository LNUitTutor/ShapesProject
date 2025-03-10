from FlatShapes import Circle

class Cylinder:
    def __init__(self, radius = 1, height = 1):
        self.base = Circle(radius)
        self.height = height
    def __str__(self):
        return f'Cylinder[r = {self.base.r}, h = {self.height}]'
    def Volume(self):
        return self.base.area()*self.height
    def LateralArea(self):
        return self.base.perim()*self.height
    def BaseArea(self):
        return self.base.area()
    def TotalArea(self):
        return 2*self.BaseArea()+self.LateralArea()
        

if __name__ == '__main__':
    a = Cylinder()
    b = Cylinder(5, 8)
    print(a)
    print('v=', a.Volume(),'s=', a.TotalArea())
    print(b)
    print('v=', b.Volume(),'s=', b.TotalArea())
    
