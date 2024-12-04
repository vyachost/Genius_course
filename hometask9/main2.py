# Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)
#   Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс, наприклад, "Коло" (Circle) та "Прямокутник" (Rectangle). 
#   Потім додайте новий клас, який розраховує площу будь-якої фігури, не модифікуючи існуючі класи. 
#   Використовуйте принцип OCP для розширення функціональності.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def square(self):
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def square(self):
        return pi * (self.radius)**2
    
class Rectangle(Shape):
    def __init__(self, a, b) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b