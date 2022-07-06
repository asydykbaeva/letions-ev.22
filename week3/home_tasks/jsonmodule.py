# # # # Работа с файлами 
# # # # Каретка - Указатель
# # # # Hello world 

# # # #Работа с файлами
# # # # file open
# # # import json
# # # from msilib.schema import Patch
# # # from operator import index
# # # import readline
# # # import string
# # # from urllib import request
# # # from winsound import SND_NOWAIT

# # # from numpy import append

# # # open (<Patch to our file>)

# # # file = open ('/home/........')
# # # file = open ('files.py')


# # # Режимы  (методы) для работы с файлами:
# # # 1. r/ r+ (read)
# # # 2. w/ w+ (write)
# # # 3. a/ a+ (append) - добавление/изменение

# # # # file= open('text.txt')
# # # # data = file.read ()
# # # # data = data.split('\n')
# # # # print(data)
# # # # print(type(data))
# # # # file.close() - обязательно закрываем файл


# # # # .readlines() - если указ



# # # dumps  - n
# # # dump 
# # # load - метод кторый считывает вы формате json и переводлит его в объект python
# # # loads -  метод который считывает JSON в текстовом формате и переводит его в объект python 


# # # #-----------------
# # # процесс десериализации
# # # import json
# # # from urllib.request import request.urlopen
# # # data = request.urlopen('https://randomuser.me/api/')
# # # print(type(data))
# # # print(data)


# # from dataclasses import dataclass
# # import json
# # from lib2to3.pgen2.pgen import generate_grammar


# # generate_to_dict = json.load(data)
# # print(generate_to_dict)
# # print(type(generate_to_dict))


# #-------------------------------------
# процесс сериализации

# import json
# dict _= {
#     'name':'John', 'last_name': 'Snow'
#     'status':True,
#     'wife': none,
#     'children':False
# }

# with open ('new.json','w') as file:
#     json.dumps(dict_,file)


from ast import Delete
import json
from turtle import update
from venv import create
dict _= {
    'name':'John', 'last_name': 'Snow'
    'status':True,
    'wife': none,
    'children':False
}
str = json.dumps(dict_)
print(str)
print(type(str))



CRUD - Create Read/Retriew Update Delete

