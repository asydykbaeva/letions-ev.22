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


# # # # .readlines() - если указать парметр цифрой , то выдаст в байтах кол-во
# # # # file = open('full path')
# # # # data = file.readlines()
# # # # print(data)


# # # .write -  в данном режиме сперва удаляет даннные файла, после записывает
# # # file = open('text.txt', 'w')
# # # data = file.write ('Hello world! \n My name is John!\n King')
# # # print(data)
# # # file.close() 


# # # .append - добавление новых даннных
# # # # file = open('text.txt', 'a')
# # # # file.write('\nJohn Snow bastard and King!')
# # # # file.close() 

# # # # file = open('text.txt', 'r')
# # # # file.close() 

# # # # file = open('text.txt', 'a')
# # # # file.close() 

# # # # file = open('text.txt', 'x') - для создания, проверив на существование
# # # # file.close() 


# # # #Контекстный менеджер
# # # with open ('text.txt','r') as file:
# # #     data = file.read()
# # #     print(data)

# # # # Разница м\у write  и writelines

# # # file.tell() - возвращает индекс, где находится указатель(каретка)


# # # file.seek (<int>) - перемещает каретку на указанный int(index)

# # # from PIL import Image
# # # import pytesseract
# # # import re

# # # def get_imei_codes(list_):
# # #     list_of_imei = []
# # #     for image in list_images:
# # #         string = pytesseract.image_to_string(image)
# # #         print(string)
# # #         llist_of_imei.append(re.findall(r'IMEI'.\d.\s\d+', string
# # #         '))
# # # with open ('imeicodes.txt','w') as file:
# # # for x in list_of_imei:
# # #     for x in x:
# # #         file.write(f'{i}\n')
# # # list_images = ['imei.jpg']
# # # get_imei_codes (list_images)
# # # регексы - прочитать



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


import json
dict _= {
    'name':'John', 'last_name': 'Snow'
    'status':True,
    'wife': none,
    'children':False
}
str = json.dumps(dict_)
print(str)
print(type(str))
