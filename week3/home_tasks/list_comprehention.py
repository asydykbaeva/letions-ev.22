https://classroom.google.com/c/MzYzMzIzMjAzODEz/a/MzYzMzIzMjA0MjE2/details
'''
1. Создайте список из целых чисел от 1 до 100. Нужно использовать comprehension.
'''
# 1.
# a =  [i for i in range(100)]
# print(a)
# 2.
# # a = range (1,100)
# # print(list(a))


'''
2. Создайте список из нечётных целых чисел в промежутке от 1 до 50. Нужно использовать comprehension.
'''
# 1.
# a =  [i for i in range(1,50,2)]
# print(a)
2.
# a =  [i for i in range(1,50) if i%2 != 0]
# print(a)
'''
3. Создайте список используя int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4] и запишите в новый список только четные числа, которые больше нуля. Нужно использовать comprehension.
'''
# int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# new_list = [i for i in int_list if i>0 and i%2 == 0]
# print (new_list)
'''
4. Создайте список из квадратов всех чисел от 1 до 25 (включительно). Нужно использовать comprehension.
'''
1.
# new_list = [i**2 for i in range(1,26)]
# print (new_list)

2.
# int_list = range(1,26)
# new_list = [i**2 for i in int_list]
# print (new_list) 
'''
5. Объявите новый список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] и конвертируйте строковые данные в целочисленные. Нужно использовать comprehension.
'''
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# new_list =[int(i) for i in str_list]
# print(new_list)
'''
6. Пройдитесь по промежутку чисел от 1 до 10 (включительно), если число нечётное, запишите в список само число, если же чётное, то квадрат этого числа. Нужно использовать comprehension.
'''
1.
# a = [i**2 if i % 2 != 1 else i for i in range(1, 11)]
# print(a)

2.
# a= [pow(i, 2) if i % 2 == 0 else i for i in range(1, 11)]
# print(a)

3.
# a = [i*i if not i % 2  else i for i in range(1,11)]
# print(a)

'''
7. Пройдитесь по промежутку чисел от 1 до 10 и запишите в список True, если число чётное и False в противном случае. Нужно использовать comprehension.
'''
1. 
# a = [True if  i % 2 != 1 else False for i in range(1,11)]
# print(a)

2.
# a = [bool(1) if not num % 2 else bool(0) for num in range(1, 11)]
# print(a)
'''
8. Создайте список из 10 произвольных имён, затем пройдитесь по данному списку и  если имя состоит меньше чем из 4 букв замените имя на 'shorter', а если больше на 'longer'. Нужно использовать comprehension.
'''
# list = ['Ann','John','David','Zoe','Ian','Oscar','Oliver','Ava','Grace','Theodore']
# updated_list = ['longer' if len(i) >= 4  else 'shorter' for  i in list]
# print (updated_list)

'''
9. Дано предложение 'In 1984 there were 13 instances of a protest with over 1000 people attending'. Получите список чисел из этого предложения. Нужно использовать comprehension.
'''
# str = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# num_list = [num for num in str.split() if num.isdigit()]
# print(num_list)


