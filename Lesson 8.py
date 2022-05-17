from abc import ABC, abstractmethod
print('Задача 1:"ф')
print()
class Animal(ABC):
    name: str

    def __init__(self, name):
        self.name = name
    @abstractmethod
    def says(self):
        pass

class Cat(Animal):

    def says(self):
        return f"{ self.name} - кошка. Говорит МЯУ! "

class Dog(Animal):

    def says(self):
        return f"{ self.name} - собака. Говорит ГАВ! "


class Cow(Animal):

    def says(self):
        return f"{ self.name} - корова. Говорит МУ! "

cat = Cat('Маркиза')
dog = Dog('Шарик')
cow = Cow('Бурёнка')

print(cat.says())
print(dog.says())
print(cow.says())

print()
print('Задача 2:')
print()
from math import *

class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        raise NotImplemented
    @abstractmethod
    def get_square(self):
        raise NotImplemented

class Circle(Shape):
    r: float

    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        return 2 * pi * self.r

    def get_square(self):
        return pi * self.r ** 2

class Rectangle(Shape):
    a: float
    b: float

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return 2 * (self.a * self.b)

    def get_square(self):
        return self.a * self.b

class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    def get_perimeter(self):
        return 4 * self.a

    def get_square(self):
        return self.a ** 2

rad = Circle(r=3)
ab = Rectangle(a=3, b=4)
aa = Square(a=5)
print('Периметр круга:', '{:.2f}'.format(rad.get_perimeter()))
print('Площадь круга:', '{:.2f}'.format(rad.get_square()))
print('Периметр прямоугольника:', '{:.2f}'.format(ab.get_perimeter()))
print('Площадь прямоугольника:', '{:.2f}'.format(ab.get_square()))
print('Периметр квадрата:', '{:.2f}'.format(aa.get_perimeter()))
print('Площадь квадрата:', '{:.2f}'.format(aa.get_square()))



