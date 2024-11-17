# У цьому модулі створіть наступні функції:
# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.

def calculate_average(numbers):
    if len(numbers) > 0: return sum(numbers)/len(numbers)
    else: print('Список не має бути пустим')

def find_max(numbers):
    if len(numbers) > 0: return max(numbers)
    else: print('Список не має бути пустим')
