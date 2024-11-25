# Завдання 2: Абстракція
# 
#     Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).
#     Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle). 
#         У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.
# 
# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def calculate_area(self):
        return pi * (self.radius)**2

class Rectangle(Shape):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def calculate_area(self):
        return self.a*self.b

class Triangle(Shape):
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def calculate_area(self):
        p = (self.a + self.b + self.c)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**(0.5)

circle1 = Circle(5)
print('Area of circle:', circle1.calculate_area())
rec1 = Rectangle(5, 6)
print('Area of rectangle:', rec1.calculate_area())
tri1 = Triangle(5, 6, 7)
print('Area of triangle:', tri1.calculate_area())