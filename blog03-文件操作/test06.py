#-*- coding:utf-8 -*-
class Rect:
    def __init__(self, length, width):
        self.length = length;
        self.width = width;

    def detail(self):
        print(self.length, self.width)

    def showArea(self):
        area = self.length * self.width
        return area

    def showCir(self):
        cir = (self.length + self.width) * 2
        return cir
#执行
rect1 = Rect(4,5)
rect1.detail()
area = rect1.showArea()
cir = rect1.showCir()
print('面积:', area)
print('周长:', cir)
