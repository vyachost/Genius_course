# 1. **Перевірка паролю:**
# Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, 
# чи введений користувачем пароль співпадає з ним. Якщо пароль дорівнює "password123", 
# виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".

password = "password123"
passwordYes = False
while not passwordYes:
    strInput = input('Input password:')
    passwordYes = password == strInput
    if not passwordYes: print("Неправильний пароль")
print("Ви увійшли в систему")