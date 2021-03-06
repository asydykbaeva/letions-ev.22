https://replit.com/@AidanSydykbaeva/built-ins-hw-3#main.py



# Встроенные функции. Map, filter, reduce, zip. lambda



"""
Решение задач с помощью встроенной функции map.

Условие: дан список чисел - nums = [1, 2, 3, 4, 5, 6, 7],  возведите все числа в третью степень, используя встроенную функцию. 
 
По условию нам нужно взять каждое число из списка nums и возвести его в степень. Значит нужно применить какую-то функцию и преобразовать элементы нашего списка. Для этого идеально подходит встроенная функция map. Вспоминаем что map принимает первым аргументом функцию, а вторым последовательность - т.е список nums. 
В качестве функции можем написать lambda выражение. Прописываем ключевое слово lambda, указываем переменную x, куда будет подставляться каждое из чисел в нашем списке nums, далее через двоеточие пишем что должна сделать lambda - 
x ** 3 ( ** - арифметический оператор возводящий в степень):

lambda x : x ** 3

Наша функция готова, теперь передаем ее в map вместе со списком nums:

map(lambda x: x ** 3, nums)

Оборачиваем все выражение во встроенную функцию list, чтобы преобразовать map объект в список и сохраняем в переменной new_nums(любое название):

new_nums = list(map(lambda x: x ** 3, nums))

Распечатываем результат:
    print(new_nums)

Получаем:
    [1, 8, 27, 64, 125, 216, 343]

"""

"""
1. Дан список, состоящий из чисел. Создайте новый список, состоящий из квадратов этих чисел.
"""

# list1 = [1, 2, 3, 4, 5, 6, 7] 
# list2 = list(map(lambda x : pow(x,2), list1))
# print (list2)
"""
2. Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0, замените его на False, если больше, то на True.
"""

# list_ = [-1, 2, 3, 0, 5, -3, 7]
# list2 = list(map(lambda x :  x>0, list_))
# print (list2)

"""
Использование filter().

Условие: дан список со строками - fruits = ['apple', 'banana', 'grapes', 'apricot'], отфильтруйте список и оставьте в нем только те слова которые начинаются на букву А.

В этой задаче уже по условию понятно что нам нужно использовать функцию filter. filter принимает в качестве первого аргумента функцию возвращающую True либо False, а вторым аргументом - последовательность. В качестве функции также можем написать lambda, обозначим переменную word для каждого слова в нашем списке:

lambda word

через двоеточие прописываем условие, так как в нашей переменной word будет хранится строка, и нам нужно отобрать только те строки которые начинаются с буквы А, мы можем применить строковый метод startswith(метод строк, принимающий в аргументы строку с которой должно начинаться наше слово в нашем случае ‘a’ ):

lambda word : word.startswith('a')

Теперь в нашу переменную word по одному будет попадать каждая наша строка из fruits и если word.startswith(‘a’) будет возвращать True то данные слова будут отбираться из списка таким образом: 
    lambda ‘apple’ : ‘apple’.startswith('a') → True  
отбираем в наш новый список
    lambda ‘banana’ : ‘banana’’.startswith('a') → False 
 убираем, т.к возвратил False
 

Функция у нас готова, последовательность fruits есть, можем подставить аргументы в filter:
filter(lambda x: x.startswith('a') ,words)
Теперь преобразуем filter объект в список с помощью встроенной функции list и сохраним отфильтрованный список в новой переменной a_words:

a_words = list(filter(lambda word:word.startswith('a') , fruits))

Распечатаем результат:
    print(a_words)
 Получаем:
    ['apple', 'apricot']

"""




"""
3. Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.
"""

# list_ = [-1, 2, 3, 0, 5, -3, 7]
# a = list(filter(lambda i :  i%2==0, list_))
# print(a)


"""
4. Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.
"""
1.
# fruits = ['apple1', 'banana22', 'grapes333', 'apricot4444']
# i_len = (list(filter(lambda i : len(i) > 7,fruits)))
# print(i_len)

2.
# list_ = ['apple1', 'banana22', 'grapes333', 'apricot4444']
# i_len = lambda i : len(i) > 7
# i_len_list = list(filter(i_len,list_))
# print(i_len_list)

"""
5. Дан список, с числами. Посчитайте количество чётных и нечётных чисел в этом списке.
"""
# 1.
# list_ = [1, 2, 3, 0, 5, 3, 7]
# a = list(filter(lambda num: num %2 == 0,list_))
# b = list(filter(lambda num: num %2  == 1,list_))
# res = 'even'+ str(len(a)) + 'odd' + str(len(b))
# print(res)

# ls= [1, 2, 3, 0, 5, 3, 7]
# a = list(filter(lambda num: num % 2 == 0, ls))
# b = list(filter(lambda num: num % 2 != 0, ls))
# res = f'even: {len(a)}, odd: {len(b)}'
# print(res)




""" 
6. Дан список из чисел. Проверьте,все ли числа больше трёх.
"""
# 1.
# ls= [1, 2, 3, 0, 5, 3, 7]
# res = not any(map(lambda num: num < 3, ls))
# print(res)

# 2.
# ls= [1, 2, 3, 0, 5, 3, 7]
# res = all(i > 3 for i in ls)
# print(res)


"""
7. Даны списки из чисел. Проверьте,есть ли в нем отрицательные числа.
"""

# list_ = [-1, 2, 3, 0, 5, -3, 7]
# a = any (i < 0 for i in list_)
# print(a)

# писать код здесь 


"""
Решение задач с помощью reduce().

Условие: дан список из строк - my_list =  [‘m’, ‘a’, ‘k’, ‘e’, ‘r’, ‘s’]. Используя функцию reduce конкатенируйте(прибавьте ‘m’ + ‘a’ . . .) все строки в списке и получите одну строку.  
 
Вспоминаем что reduce принимает два аргумента, функцию и последовательность. Давайте напишем функцию также используя анонимную функцию lambda. Мы знаем что reduce по завершению работы возвращает нам результат в виде одного объекта и нам нужно по очереди добавить каждую букву к следующей. Для этого в lambda мы можем указать две переменные, обозначающие каждые две буквы которые будут складываться вместе, скажем x и y:
lambda x, y
Теперь через двоеточие указываем что нам нужно сделать с элементами в x и y, а именно сложить их через оператор +:

    lambda x, y : x + y

reduce в свою очередь будет пропускать через эту функцию все элементы в нашем списке  my_list =  [‘m’, ‘a’, ‘k’, ‘e’, ‘r’, ‘s’]:

    lambda ‘m’, ‘a’ : ‘m’ + ‘a’  = ‘ma’

и подставлять новую строку вместо первоначальных двух:

     [‘ma’, ‘k’, ‘e’, ‘r’, ‘s’]

затем снова:

    lambda ‘ma’, ‘k’ : ‘ma’ + ‘k’  = ‘mak’
    [‘mak’, ‘e’, ‘r’, ‘s’]
    . . .
и так до тех пор пока мы не получим строку ‘makers’
 
Теперь имея функцию и наш список строк мы можем применить reduce который нужно импортировать из functools:

import functools
new_word = functools.reduce(lambda x, y: x + y, my_list)

Выведем результат в консоль:
    print(new_word)

Получаем -  ‘makers’ 
"""




"""
8. Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
"""
1.
# list_ = [1, 2, 3, 4]
# import functools 
# ls = functools.reduce(lambda x, y: x + y, list_) 
# print(ls)

# 2.
# list_ = [1, 2, 3, 4]
# res = sum(list_)
# print(res)

"""
9. Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
"""
# 1.
# list_ = [5, 6, 7, 8]
# multiple = list(map(lambda x: x*x,list_))
# print(multiple)                

# 2.
# list_ = [5, 6, 7, 8] 

# def multiple(i):
#    return i*i

# res = list(map(multiple, list_))
# print(res)


"""
10. Дан список из имён. Найдите самое длинное имя из списка, используя функцию reduce.
"""
1.
# import functools
# a = ['Мурат', 'Эржан', 'Чынгыз', 'Алтынай', 'Асема']
# b = functools.reduce(lambda word1, word2: word1  if len(word1) > len(word2) else word2,a)
# print(b)
2.
# a = ['Мурат', 'Эржан', 'Чынгыз', 'Алтынай', 'Асема']
# res = max(a, key=len)
# print(res)






