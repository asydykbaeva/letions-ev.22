from ensurepip import version


команды для установки программ/библиотек
1.brew install git
2.git version (ubuntu: git -- version)

3.git config -- global user.name "asydykbaeva"
4.git config --global user.email "a.sydykbaeva91@gmail.com"
5.cd .ssh/
6..ssh % cat id_rsa.pub
7..ssh % sudo nano id_ed25519.pub

синтаксис :git - команда - параметры
GIT (CKB) - система контроля версий
githab - webserver












from ast import comprehension
from asyncore import loop
import string
import types


Dara types

1.Numbers (числа)
2.Strings (строки)
3.Lists (списки)
4.Dictionaries (словари)
5.Tuples (кортежи)
6.Sets (множества)
7.Boolean (логический тип данных)

1.Mutable - изменяемые: 1.list - списки
                        2.dict - словари
                        3.set - > x = {"apple", "banana", "cherry"} - множества

2.inmutable - неизменяемые : 1.int  - числа
                             2.string- строки
                             3.tuple - > x = ("apple", "banana", "cherry") - кортежи
1.упорядоченные: 1.list -списки
                 2.tuple - кортежи
                 3.string - строки
                 4.dict  - словари
 
2.неупорядоченные : 1.set 

#Аннотация переменных: str, int, float, bool и None
from typing import List
name: str = 'Tommy'
age: int = 24
height_in_meters: float = 1.7
colleagues: List[str] = ['Alicia', 'John']

#Аннотация функций
Синтаксис аннотации переменных работает и для параметров функций. Однако, 
чтобы указать тип возврата (return), мы добавляем стрелку –>, за которой следует его тип.

from typing import Dict, List
def convert_celcius_to_fahrenheit(celcius_temp: float) –> float:
    return (celcius_temp * 9/5) + 32
def send_email(subject: str, body: str, recipients: List[str], cache: Dict[str, str]) –> bool:
    # пропущено для краткости
    return True  # или False

#Built-in function:
1.lambda - lambda arguments: expression
Лямбда принимает любое количество аргументов (или ни одного), но состоит из одного выражения.
>>> f = lambda x: x * x
>>> f(5)
25
>>> f = lambda x, y: x * y
>>> f(5, 2)
10
>>> f = lambda: True
>>> f()
True

2.map -  map(function, iterable, [iterable 2, iterable 3, ...]) - A lambda function is a small anonymous function,can take any number of arguments, but can only have one expression.
         Use lambda functions when an anonymous function is required for a short period of time.
         
         map(lambda item: item[] expression, iterable) - можем использовать вместо цикла for.Преимущества ает возможность применить функцию к каждому элементу итерируемого объекта. 
         Это повышает производительность, поскольку функция применяется только к одному элементу за раз без создания копий элементов в другом итерируемом объекте. Это особенно полезно при обработке больших наборов данных.
         map() — это встроенная функция Python, принимающая в качестве аргумента функцию и последовательность. Она работает так, что применяет переданную функцию к каждому элементу.

3.filter - 

4.reduce (from functools import reduce).
Параметры
Встроенная функция reduce() принимает два аргумента, функцию и последовательность.
Пример:
import functools
new_word = functools.reduce(lambda x, y: x + y, my_list)

5.numeric (from unicodedata import numeric)

6.all - all(iterable).
Пример:
item_list = [True, True, True, True]
print (all(item_list))

Встроенная функция all() проверяет все элементы последовательности на определенное условие и возвращает результат в виде булевого значения - True либо False. 
Параметры:
iterable - итерируемый объект (список, кортеж, словарь).
Возвращаемое значение:
bool - значение логического типа True или False.
Описание:
Функция all() возвращает значение True , если все элементы в итерируемом объекте - истинны, в противном случае она возвращает значение False.
Если передаваемая последовательность пуста, то функция all() также возвращает True.
Функция all() применяется для проверки на True ВСЕХ значений в последовательности 

7.any - any (tem_list)
Функция any() вызывается с аргументом итерируемого типа item_list
Функция any() возвращает значение True, если хотя бы один элемент во всём итерируемом типе истинный.
Если список полностью пуст, any() всегда будет возвращать False.
Непустые строковые значения также всегда являются истинными:

item_list = ["mango", False]
print (any(item_list))

Выдаст:True


6.input()
7.bool()
8.int()
9.str()
10.print()
11.set()
12.frozenset()
13.tuple()
14.dict()
15.list()
16.sorted()
17.sum()
18.max()
Пример:
# a = ['Мурат', 'Эржан', 'Чынгыз', 'Алтынай', 'Асема']
res = max(a, key=len) - принимает 2 параметра (итерируемый объект,можно ключем задать критерий для отбора максимального по длине к примеру)
# print(res)
19.min()
20.len()


#Basic

ВАЖНО:
- int нельзя в строку и пытаться вывести без спец.функции str
- str в int можно 





#Math_functions
 - from math import sqrt
 - pow()


 #Loop- Циклы
Пример нахождения квадрата чисел в отрезке ото 1 до 9:
# square_dict = dict()
# for num in range(1, 11):
#     square_dict[num] = num*num
# print(square_dict)


#func random, randint, randrange - случайные числа / эмуляция случайных чисел (на нем основываются комп.игры для генгерацуии случючисел)
В состав стандартной библиотеки phyton входит модуль random.Он содержит множество функций, связанных с эмуляцией случайности (например, "перемешивание" элементов последовательности), а не только функции генерации псевдослучайных чисел.
#Python Data Types
- Dict:
my_dict = {
        'key': 'value', 
        'sub_dict': {},
        2: [1, 2, 3, 4], 
    }
pow(base, exp, mod)
Параметры:
base - возводимое число,
exp - число, являющееся степенью,
mod - необязательно, число, на которое требуется произвести деление по модулю.

методы словаря:
-keys() - возращает список всех ключей словаря.
- Tuple
- String
- INTEGER
- boolean




https://www.w3schools.com/python/python_ref_string.asp
#StringMethods (str_method)  - ЗДЕСЬ ДЛЯ ВСЕХ ФУНКЦИЙ И МЕТОДОВ НЕОБХОДИМО УЗНАТЬ ПО ОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ КОТРЫЕ ПРИНИМАЕТ КАЖДАЯ ИЗ НИХ
.split() - string.split(separator, maxsplit)
'Parameter	Description
#separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

.len()
.title() - str.title() не принимает параметров.,сonverts the first character of each word to upper case 
.capitalize() - string.capitalize() не принимает параметров, eturns a string where the first character is upper case, and the rest is lower case.
.upper() - string.upper() не принимает параметров,returns a string where all characters are in upper case.
.sorted(iterable[, key][, reverse]) - Отсортированный список.

COMPREHENTION
Синтаксис: 
- list_comprehention: new_list = [expression for member in iterable]
- dict_comprehention: new_dict = {key: value for vars in iterable}
- set_comprehention:new_dict = {expression for vars in iterable}
# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)



Convert str into int via comprehension:
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# new_list =[int(i) for i in str_list]
# print(new_list)

#Тернарные выражения / Тернарные операторы



#functions/classes  - ЗДЕСЬ ДЛЯ ВСЕХ ФУНКЦИЙ И МЕТОДОВ НЕОБХОДИМО УЗНАТЬ ПО ОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ КОТРЫЕ ПРИНИМАЕТ КАЖДАЯ ИЗ НИХ
 - list()
 - tuple ()
 - int ()
 - dict ()
 - set()
 - range() - является самостоятельным объектом,<class 'range'>. Если step равен нулю, то  вызывает исключение ValueError.
 Диапазоны обеспечивают проверку вхождения, поиск по индексу, срез и отрицательную индексацию элементов.
- если не задать интервал (т.е.указать функцию range (0) - указать в параметре 0, то фунукция возвращает пустой список)
- если, указать функцию пустой, без передачи какого-либо аргумента, то возврвщает ошибку TypeError



Others:
- loop - цикл/узел/петля
 - multiply (произведение/увеличиваться)
 - divide (делиться без остатка/делить)
 - explicit (заданный в явном виде)
 - foo (иллюстрация)
 - capitalized (напечатанный прописными буквами)
 - whitespace (разделитель; пробельный символ)
 - odd - нечетное число(it-шанс)


 - идиоматический - свойственный, характерный : list[], чем list()


 Ошибки на темы:
 - map - перед map  не указала вернуть/вывести в list :ошибкка <map object at 0x7fee690a3df0>