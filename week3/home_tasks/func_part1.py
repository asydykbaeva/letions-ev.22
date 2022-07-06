
# Введение в функции. Позиционные и именованные, args kwargs, аргументы по default. 

"""
Функции.

"""

""""
1. Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# my_dict = {'data1':100,'data2':-54,'data3':247}
# result=1
# for key in my_dict:    
#     result=result * my_dict[key]
# print(result)

"""
2. Создайте функцию, которая будет принимать строку. Функция должна выводить длину этой строки.
"""

# def get_string_length('Traceback'):
# result = len(get_string_lengt)
#  return result
# print(get_string_lengt)


"""
3. Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип данных принятых аргументов.
"""


# def intro(**data):
#     print("\nData type of argument:",type(data))
#     for key, value in data.items():
#         print("{} is {}".format(key, value))
# intro(Firstname="Sita", Lastname="Sharma", Age=22)
# intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25)







  


"""
4. Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.
"""
# def divide(x,y):
#  return x/y
# print(divide(5, 10)) 

# def divide(a = 345,b = 21):
#  return  a / b
# print (divide())


"""

"""

"""
5. Создайте функцию, которая принимает словарь. Пройдитесь по словарю циклом и распечатайте все его ключи
"""
# dict_= {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# def dictionary():
#  for key in dict_ :
#      print(key)
# print(dictionary())


"""
6. Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""

# def multiply(numbers):  
#     total = 1
#     for x in numbers:
#         total *= x  
#     return total  
# print(multiply((3, -2, 4, 1, 5)))


"""
7. Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр.
"""

# def sum(numbers):  
#     total = 0
#     for x in numbers:
#         total += x  
#     return total  
# print(sum((3, 2, 4, 1, 5)))


"""

"""


"""
8. Создайте функцию, которая принимает число и выводит "It's even number" если число четное(делится на 2 без остатка - 2, 4, 20 и.т.п), если же число нечетное (3, 9 и.т.п) функция должна выводить "It's odd number".
"""

# def number(i):
#     if i %2==0:
#       print ("It's even number")
#     else :
#       print ("It's odd number")
# number (250)
  


"""
9. Создайте функцию которая принимает от пользователя два числа. Функция должна сравнить эти числа между собой и вывести максимальное значение.
"""

# a=int(input())
# b=int(input())
# def biggest(a,b):
#     if a>b:
#         print("Biggest Number =",a)
#     elif b>a:
#         print("Biggest Number =",b)
# biggest(a,b)


"""
10. Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом. Пробелы и регистр учитывать не нужно.

>Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.
"""

# def get_polindrom(list):
#     result = []
#     for word in list:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result
# list = ['deed', '112211', 'level', 'Deified', 'noon', '4556', 'sagas', 'true']
# print(get_polindrom(list))



