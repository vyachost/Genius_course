# Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)
#   Створіть ієрархію класів для геометричних фігур, де кожен підклас (наприклад, "Квадрат" і "Круг") може замінити базовий клас "Фігура" 
#   без порушення функціональності. 
#   Переконайтеся, що ці підкласи можуть використовуватися замість базового класу у всіх контекстах без проблем.

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