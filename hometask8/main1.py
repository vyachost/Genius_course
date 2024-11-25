# Завдання 1: Інкапсуляція
# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
#     Ім'я (name)
#     Електронна пошта (email)
#     Пароль (password)
# Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери). Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.

class User:
    def __init__(self, name, email, password) -> None:
        self._name = name
        self._email = email
        self._password = password
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def set_password(self, password):
        self._password = password

new_user = User('Username', 'user_email@example.com', 'a12345')

print('Name:', new_user.get_name(), 'email:', new_user.get_email())