# **Завдання 1: Наслідування**
# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:
# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.
# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. 
# Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. 
# Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.
# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.

# **Завдання 2: Поліморфізм**
# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб 
# (наприклад, "Це [виробник] [модель] [рік] року виробництва.").
# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.
# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте 
# за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.



class Vehicle:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f'Make {self.make}')
        print(f'Model {self.model}')
        print(f'Year {self.year}')
    
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type) -> None:
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print('Starting the engine.')
    
    def display_info(self):
        print(f'Make {self.make}')
        print(f'Model {self.model}')
        print(f'Year {self.year}')
        print(f'Fuel type {self.fuel_type}')


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, ) -> None:
        super().__init__(make, model, year)

    def ride_motocycle(self):
        print('Riding the motocycle')


class Bicycle(Vehicle):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)

    def ride_bicycle(self):
        print('Riding the bicycle')

car = Car('BMW', 'BMW iX', 2019, 'disel')
moto = Motorcycle('Yamaha', 'XSR900', 2020)
bicycle = Bicycle('Fiido', 'C11', 2015)

print(car.__dict__)
print(moto.__dict__)
print(bicycle.__dict__)
print()
car.display_info()
print()
moto.display_info()
print()
bicycle.display_info()