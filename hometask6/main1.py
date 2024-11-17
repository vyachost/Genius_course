# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.

import animal

animal1 = animal.Animal('Tom', 'cat', 5, 'Miau...')
animal2 = animal.Animal('Jack', 'dog', 3, 'Gau...')

print(animal1.make_sound())
print(animal2.make_sound())