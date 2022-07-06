https://replit.com/@AidanSydykbaeva/List-Set-Dict-comprehension-extra-tasks#main.py
'''
1. Создайте словарь в котором ключами будут числа, а значениями строки, перебирите словарь циклом и если ключ четный, нужно заменить его значение на длинну этого значения, если ключ нечетный то возвести длинну его значения в 3 степень, нужно работать только с одним словарем, нельзя создавать доп. словарь. Необходимо использовать dict comprehension
'''
# dict = {1: 'Bishkek', 2: 'Canberra', 3: 'Vienna', 4:'Yerevan'}
# new_dict = {key: len(val) if key % 2 == 0 else len(val) ** 3 for key, val in dict.items()}
# print(new_dict)
'''
2. Создайте 2 сета из 10 рандомных элементов(необходимо использовать random), затем объедините их, и если их длинна меньше 20, то вы должны вывести сообщение типа 'В этом сете было 3 повторения, его длинна составляет 17', 3 это количество элементов, которые были не уникальны, необходимо использовать set comprehension, на этапе создания сетов
'''
1.
# set1 = {num for num in range(10)}
# set2 = {num for num in range(10, 20)}
# full_set = set1 | set2
# if len(full_set) < 20:
#     length = len(full_set)
#     res = set1 & set2
#     print(f'В этом сете было {len(res)} повторения, его длина составляет {length}')
# else:
#     print('Ваш объединенный сет полностью уникальный!')
# 2.
# set1 = {num for num in range(10)}
# set2 = {num for num in range(10, 20)}
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     length = len(full_set)
#     res = set1.intersection(set2)
#     print(f"В этом сете было {len(res)} повторения, его длина составляет {length}")
# elif len(full_set) == 20:
#     print("Ваш объединенный сет полностью уникальный!")


'''
3. Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты. Нужно использовать comprehension.
'''
# dict = {key:pow(key,2) for key in range(1,10)}
# print(dict)
'''
4. Запросите у пользователя число от 1 до 10. Затем пройдитесь по промежутку чисел от 1 до 500 и запишите в словарь только те числа, которые кратны числу, которое ввел пользователь. Ключом будет само число, а значением его квадрат. Нужно использовать comprehension.
'''
1.
# a = int(input())
# dict = {num: pow(num, 2) for num in range(1, 501) if num % a == 0}
# print(dict)
2.
# a = int(input())
# dict = {num: num * num for num in range(1, 501) if not num % a}
# print(dict)
'''
5. Дан словарь, в котором значениями являются целые числа. Пройдитесь по элементам и замените значения на список чисел от 1 до числа, которое является значением. Нужно использовать comprehension.
Например: a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} -> {'a': [1], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4], 'd': [1, 2, 3]}
'''
1.
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict = {key: list(range(1, val+ 1)) for key, val in a.items()}
# print(dict)
2.
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict = {key: [num for num in range(1, val + 1)] for key, val in a.items()}
# print(dict)


'''
6. Создайте словарь, где ключами будут строки, а значениями произвольные числа. Затем пройдитесь по элементам и запишите вместо значения строку 'even', если значение четное, а если нет то 'odd'. Нужно использовать comprehension.
'''
# dict = {'march': 3, 'april': 4, 'may': 5,'june':6}
# a = {key: 'even' if val % 2 == 0 else 'odd' for key, val in dict.items()}
# print(a)
'''
7. Дано предложение 'In 1984 there were 13 instances of a protest with over 1000 people attending'. Получите список чисел из этого предложения. Нужно использовать comprehension.
'''
1.
# a = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# b = [num for num in a.split() if num.isdigit()]
# print(b)

# 2.
# a = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# b= [num for num in a.split() if num.isnumeric()]
# print(b)

'''
8. Дан словарь, в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам. Замените оценки названием предмета, по которому студент имеет высший балл. Нужно использовать comprehension.
Например: a = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
Результат: {'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}
'''
# a = {
# 'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}
# }
# b = {key1: [key2 for key2 in val1.keys() if val1[key2] == max(val1.values())][0] for key1, val1 in a.items()}
# print(b)

# a= {
#   'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}
# }
# b = {key1: key2 for key1, val1 in a.items() for key2, val2 in val1.items() if val2 == max(val1.values())}
# print(b)



'''
9. Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Нужно использовать comprehension.
Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
'''
1.
# my_dict = {
#     'first': {'a': 1}, 
#     'second': {'b': 2}
# }
# new_dict = {key1: val2 for key1, val1 in my_dict.items() for val2 in val1.values()}
# print(new_dict)

2.# my_dict = {
#     'first': {'a': 1}, 
#     'second': {'b': 2}
# }
# new_dict = {key1: [val2 for val2 in val1.values()][0] for key1, val1 in my_dict.items()}
# print(new_dict)and

#Для примера через dict_comprehention:
a = {i:i**2 for i in range(1,11)}
print(a)

#Через loop(через цикл  for):
a = {}
for i in range(1,11)
    a[i] = i**2
print(a)