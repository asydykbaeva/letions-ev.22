#https://replit.com/@AidanSydykbaeva/Dictionary-tasks-2#main.py
'''
1. Создайте словарь и выведите один из ключей.
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#b = list(a.keys())[0]
#print(b)
'''
2. Создайте словарь с любыми элементами, удалите один из элементов и распечатайте удалённый элемент.
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#print(a.pop('x'))
'''
3. Создайте словарь, добавьте в него новую пару ключ: значение и распечатайте.
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#a.setdefault('l', 4)
#print(a)
'''
4. Создайте словарь, удалите всего его элементы и распечатайте результат.
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#print(a.clear())
'''
5. Создайте словарь, выведите все его ключи.
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#b = list(a.keys())
#print(b)
'''
6. Создайте словарь, сделайте его копию и распечатайте её.
'''
#import copy
#a = {'x': 1, 'y': 2, 'z': 3}
#b = copy.deepcopy(a)
#print(b)
'''
7. Дан словарь, нужно перебрать его и распечатать все ключи.
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#for key in a.keys():
#    print(key)
'''
8. Создайте словарь, перебирите его и распечатайте все значения
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#for value in a.values():
#    print(value)
    
'''
9. Создайте словарь с числовыми значениями, пройдитесь по элементам и замените все чётные числа на число 2.
Пример: Ввод -> a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
        Вывод -> a{'a': 1, 'b': 2, 'c': 1, 'd': 5,  'e': 2}
'''
#a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
#b = {}
#for k, v in a.items():
#    if v % 2 == 0:
#        b[k] = 2
#    else:
#        b[k] = v
#print(b)
'''
10. Дан словарь, удалите из него все элементы с пустыми значениями.
Пример: a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} ->
          {'b': 1, 'c': 2, 'e': 3}
'''
#a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
#for k, v in list(a.items()):
#    if v == None:
#        a.pop(k)
#print(a)
'''
11. Создайте словарь, где ключами будут названия товаров, а значениями их цены,  затем, его нужно перебрать циклом и поменяйте все значения элементов, разделив их на 5
'''
#a = {'item1': 4.50, 'item2': 1.25, 'item3': 7.00}
#for k, v in a.items():
#    a[k] = v / 5
#print(a)
'''
12. Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
'''
#a = {'mango': 4, 'banana': 8, 'orange': 7}
#for k, v in list(a.items()):
#    if v % 2 == 0:
#        a.pop(k)
#print(a)
'''
13. Создайте словарь, а затем поменяйте местами ключи и значения. Распечайте полученный результат.
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#for k, v in list(a.items()):
#    del a[k]
#    a[v] = k
#print(a)
'''
14. Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
'''
#a = {'x': 1, 'y': 2, 'z': 3}
#b = sum(a.values())
#print(b)
'''
15. Создайте словарь тремя возможными способами.
'''
#a1 = {"a": 3}
#a2 = dict(key = '1')
#a3 = dict.fromkeys(['z', 'y'])

