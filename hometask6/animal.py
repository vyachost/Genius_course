# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:
# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.

class Animal:
    def __init__(self, name, species, age, sound) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"Hello, my name is {self.name} and I make sound {self.sound}."

