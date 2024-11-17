# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` і використовує його функції для виконання обчислень. 
# Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), і виведіть результат обчислення.

import calculator

a = float(input('Введіть перше число:'))
b = float(input('Введіть друге число:'))

operand = input('Введіть операцію ( + , - , * , /):')

if operand == '+': print(a, operand, b, '=', calculator.add(a, b))
elif operand == '-': print(a, operand, b, '=', calculator.subtract(a, b))
elif operand == '*': print(a, operand, b, '=', calculator.multiply(a, b))
elif operand == '/': print(a, operand, b, '=', calculator.divide(a, b))
else: print('Невідома операця')