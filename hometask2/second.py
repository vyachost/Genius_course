# 1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
# 2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі

# string
str_1 = 'First string'
str_2 = 'Second string'
print(type(str_1))
print(str_1 == str_2)

# integer
num_1 = 5
num_2 = 6
print(type(num_1))
print(num_1 > num_2)

# float
num_3  = 3.14
num_4 = 5.65
print(type(num_3))
print(num_3 < num_4)

# bool
bool_1 = True
bool_2 = False
print(type(bool_1))
print(bool_1 - bool_2)

# list
list_1 = [0, 1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', 'd']
print(type(list_1))
print(list_1 + list_2)
list_2.append('e')
print(list_2)

# dict
dict_1 = {'a': 50, 'b': 100}
dict_2 = {'c': '150', 'd': '200'}
print(type(dict_1))
print(dict_1.keys())
print(dict_2.items())

# tuple
tup_1 = (1, 2, 3, 4, 5)
tup_2 = ('a', 'b', 'c', 'd')
print(type(tup_1))
print(len(tup_2))

# None
x = None
print(type(x))
print()

# 3. Використати вивчені функції Python:
# Робота з рядками:

#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
str_1 = str(num_str)
print('type:', type(str_1))

#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
message = message.replace('y', '0')
message = message.replace('i', '1')
print('message:', message)

#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
string_join = ' '.join(split_test.split())
print('string_join:', string_join)

#  4. Визначити довжину рядку string_join за допомогою функції len()
print('довжинa рядку string_join:', len(string_join))

# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print('list_append:', list_append)

#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print('list_extend:', list_extend)

#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
print('індекс елемента 6 у списку list_extend:', list_extend.index(6))

#  4. Визначити довжину списку list_append за допомогою функції len()
print('довжинa списку list_append:', len(list_append))

# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print('car:', dict_test['car'])
print('where:', dict_test['where'])

#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
print('keys:', dict_test.keys())
print('values:', dict_test.values())

#  3. За допомогою функції items() вивести на екран пари ключ - значення
print('items:', dict_test.items())
