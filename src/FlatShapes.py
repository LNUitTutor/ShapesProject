# Оголосити клас, що моделює геометричну фігуру прямокутник
# Прямокутник уміє повідомляти свої площу та периметр
# Прямокутники порівнюють за площею

class Rectangle:
    def __init__(self,width=3,length=4):
        self.a=width
        self.b=length
    def __str__(self):
        return f'rectangle:{self.a}x{self.b}'
    def area(self):
        return self.a*self.b
    def perim(self):
        return 2*(self.a+self.b)
    def __gt__(self, other):
        return self.area() > other.area()

# Оголосіть клас, що моделює квадрат

class Square(Rectangle):
    def __init__(self,a=1):
        Rectangle.__init__(self, a, a)
    def __str__(self):
        return f'square:{self.a}x{self.a}'



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
    print(max(P,R,S))

