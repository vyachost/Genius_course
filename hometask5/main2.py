# створіть інший Python-файл (наприклад, `main.py`), який імпортує модуль `utilities.py` 
# і використовує його функції для обробки списку чисел.

import utilities

l = [1, 2, 3, 4, 5]
m = []

print('List:', l)
print('Average:', utilities.calculate_average(l))
print('Max:', utilities.find_max(l))

print('List:', m)
print('Average:', utilities.calculate_average(m))
print('Max:', utilities.find_max(m))
