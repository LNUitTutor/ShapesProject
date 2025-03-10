from FlatShapes import Circle

class Cylinder:
    def __init__(self, radius = 1, height = 1):
        self.base = Circle(radius)
        self.height = height
    def __str__(self):
        return f'Cylinder[r = {self.base.r}, h = {self.height}]'

if __name__ == '__main__':
    a = Cylinder()
    b = Cylinder(5, 8)
    print(a)
    print(b)
