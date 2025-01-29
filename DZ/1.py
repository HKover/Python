# 1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
# 2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
# 3. Використати вивчені функції Python:
# Робота з рядками:

#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити  
# усі букви 'y' на '0' та 'i' на '1'.
#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за 
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
#  4. Визначити довжину рядку string_join за допомогою функції len()

# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
#  4. Визначити довжину списку list_append за допомогою функції len()

# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
#  3. За допомогою функції items() вивести на екран пари ключ - значення

# # ======================================================================================================================================================================
# Давайте по черзі розглянемо, як створити змінні різних типів, порівняти їх і використовувати вивчені функції Python.

# ### 1. Створення змінних різних типів:

# # Створення змінних
# string = "Hello, World!"   # рядок
# integer = 42                # ціле число
# float_num = 3.14            # число з плаваючою комою
# bool_val = True             # булеве значення
# my_list = [1, 2, 3, 4]      # список
# my_dict = {"key": "value"}  # словник
# my_tuple = (10, 20, 30)     # кортеж
# none_value = None           # None (відсутність значення)
# ```

# ### 2. Порівняння між собою різних типів:

# Тепер давайте порівняємо числа, рядки, булеві значення, списки, словники та кортежі за допомогою операторів порівняння.

# ```python
# # Порівняння чисел
# print(integer == float_num)  # False, 42 != 3.14
# print(integer != 42)         # False
# print(float_num > integer)   # False

# # Порівняння рядків
# print(string == "Hello, World!")  # True
# print(string != "hello, world!")  # True

# # Порівняння булевих значень
# print(bool_val == True)    # True
# print(bool_val != False)   # True

# # Порівняння списків
# print(my_list == [1, 2, 3, 4])    # True
# print(my_list != [1, 2, 3])       # True
# print(my_list < [1, 2, 3, 5])     # True, порівняння по елементах

# # Порівняння словників
# print(my_dict == {"key": "value"})  # True
# print(my_dict != {"key": "different_value"})  # True

# # Порівняння кортежів
# print(my_tuple == (10, 20, 30))  # True
# print(my_tuple != (10, 20, 25))  # True
# ```

# ### 3. Використання вивчених функцій Python:

# Ось кілька прикладів використання різних функцій Python:

# # Функція len() для отримання довжини
# print(len(string))  # довжина рядка: 13
# print(len(my_list))  # довжина списку: 4

# # Функція type() для отримання типу змінної
# print(type(integer))    # <class 'int'>
# print(type(bool_val))   # <class 'bool'>
# print(type(my_tuple))   # <class 'tuple'>

# # Функція max() та min() для пошуку максимального та мінімального значення
# print(max(my_list))   # 4
# print(min(my_list))   # 1

# # Функція sum() для обчислення суми елементів списку
# print(sum(my_list))   # 10

# # Функція sorted() для сортування списку
# sorted_list = sorted(my_list)
# print(sorted_list)    # [1, 2, 3, 4]

# # Функція str() для перетворення на рядок
# print(str(integer))   # '42'

# # Функція abs() для отримання абсолютного значення
# negative_num = -25
# print(abs(negative_num))  # 25

# # Функція all() для перевірки, чи всі елементи списку істинні
# print(all([True, True, False]))  # False
# print(all([True, True, True]))   # True

# # Функція any() для перевірки, чи хоча б один елемент істинний
# print(any([False, False, True]))  # True
# print(any([False, False, False])) # False


# Цей код охоплює основні типи даних, оператори порівняння та деякі корисні функції в Python. Сподіваюся, це допомогло! Якщо потрібна додаткова допомога, не соромтеся запитувати!

















# ============================================================
num_str = 125


user_balance = ' , you balance'

print(str(num_str) + user_balance)


# ----------------------------------
message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')
print(message)


# ----------------------------------

split_test = 'This is a split test'
split_test = split_test.split()
print(split_test)

string_join = ' '.join(split_test)
print(string_join)
# ----------------------------------

print(len(string_join))

# ----------------------------------


