# Оголосити клас, що моделює геометричну фігуру прямокутник
# Прямокутник уміє повідомляти свої площу та периметр

class Rectangle:
    def __init__(self,width,length):
        self.a=width
        self.b=length
    def __str__(self):
        return f'rectangle:{self.a}x{self.b}'
    def area(self):
        return self.a*self.b
    def perim(self):
        return 2*(self.a+self.b)
