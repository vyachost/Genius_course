# 2. **Визначення днів тижня:**
# Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. 
# Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.
numDay = int(input('Введіть номер дня тижня(1-7):'))
if numDay == 1: print('понеділок')
elif numDay == 2: print('вівторок')
elif numDay == 3: print('середа')
elif numDay == 4: print('четвер')
elif numDay == 5: print("п'ятниця")
elif numDay == 6: print('субота')
elif numDay == 7: print('неділя')
else: print('Ви ввели неправильний номер')