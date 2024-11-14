# **Пошук простих чисел:**
#    Завдання: Знайдіть всі прості числа в заданому діапазоні.
a = int(input('введіть початок діапазону:'))
b = int(input('введіть кінець діапазону:'))
if a < b:
    i = a
    while i <= b:
        if 0 <= i <= 2: print(i)
        else:
            j = 2
            prime = True
            while j < i**(0.5)+1:
                if i % j == 0: prime = False
                j = j + 1
            if prime: print(i)
        i = i + 1
else: print('Неправильний діапазон')
