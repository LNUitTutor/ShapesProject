import math
from abc import ABC, abstractmethod

# Абстрактний клас пов'язує всі типи плоских фігур
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perim(self):
        pass
    def __gt__(self, other):
        return self.area() > other.area()

# Оголосити клас, що моделює геометричну фігуру прямокутник
# Прямокутник уміє повідомляти свої площу та периметр
# Прямокутники порівнюють за площею

class Rectangle(Shape):
    def __init__(self,width=3,length=4):
        self.a=width
        self.b=length
    def __str__(self):
        return f'rectangle:{self.a}x{self.b}'
    def area(self):
        return self.a*self.b
    def perim(self):
        return 2*(self.a+self.b)

# Оголосіть клас, що моделює квадрат

class Square(Rectangle):
    def __init__(self,a=1):
        Rectangle.__init__(self, a, a)
    def __str__(self):
        return f'square:{self.a}x{self.a}'

# Оголосіть класи, що моделюють круг і трикутник
# Об'єднайте всі класи в одну ієрархію

class Circle(Shape):
    def __init__(self,radius=2):
        self.r=radius
    def __str__(self):
        return f'circle:{self.r}'
    def area(self):
        return math.pi * self.r**2
    def perim(self):
        return 2 * math.pi * self.r 



if __name__ == '__main__':
    R = Rectangle(2,3)
    print(R)
    print('S =', R.area())
    print('P =', R.perim())
    P = Rectangle()
    print(P)
    print('S =', P.area())
    print('P =', P.perim())
    S = Square(5)
    print(S)
    print('S =', S.area())
    print('P =', S.perim())
    C = Circle(3)
    print(C)
    print('S =', C.area())
    print('P =', C.perim())
    print(max(P,R,S,C))

