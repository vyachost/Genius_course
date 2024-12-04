# Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)
# Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP. 
#   В цьому класі повинні бути методи для створення користувача, оновлення даних користувача та видалення користувача. 
#   Переконайтеся, що кожен метод відповідає за одну конкретну функцію.



class User:

    def __init__(self) -> None:
        self.users = []
    
    def __str__(self) -> str:
        return '\n'.join(self.users)
    
    def addUser(self, name, email):
        self.users.append(f"{name}: {email}")
    
    def updateEmail(self, name, oldemail, newemail):
        self.users[self.users.index(f"{name}: {oldemail}")] = f"{name}: {newemail}"
    
    def deleteUser(self, name, email):
        del self.users[self.users.index(f"{name}: {email}")]

user1 = User()
user1.addUser('Ivan', 'ivan@hotmail.com')
user1.addUser('Pedro', 'pedro@hotmail.com')
print(user1)
print()
user1.updateEmail('Ivan', 'ivan@hotmail.com', 'ivan_new@gmail.com')
print(user1)
print()
user1.deleteUser('Pedro', 'pedro@hotmail.com')
print(user1)