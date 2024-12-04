# Завдання 4: Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)
#   Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), який включає методи для друку, сканування та копіювання. 
#   Потім створіть два класи: "Принтер" (Printer) та "Сканер" (Scanner), які реалізують цей інтерфейс та використовують лише ті методи, 
#   які їм потрібні. Переконайтеся, що жоден з класів не має пустого методу.

from abc import ABC, abstractmethod

class NetworkPrinter(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def scan(self):
        pass

class Printer(NetworkPrinter):
    def __init__(self) -> None:
        super().__init__()
    
    def print(self):
        return "Printer"

class Scaner(NetworkPrinter):
    def __init__(self) -> None:
        super().__init__()
    
    def scan(self):
        return "Scaner"

