#generatogy spiska - list comprehenssions
#from ast import Expression, comprehension



#new_list = [expression for item in iterable <if condition==True>]
#list - comprehension - eto uprashennyi podhod k sozdaniu spiskov kotoryi zadeistvuet cikl for a takje instrukcii if else dlya opredeleniya togo chto v itoge okaj.dobavleno v spisok


#ls = []
#for i in range(0,100,2):
#    ls.append(i)
# print(ls)

# new_ls = [i for i in range(0,100,2)]
# print(new_ls)

# ls = [i **2 for i in range(0,11)]
# print(ls)

# fruits = ['apple', 'banana' , 'mango']
# #ls = [x.capitalize() for x in fruits]
# #print(ls)

# #ls = [x for x in fruits if x=='cherry'] - rabotaet s cel'u filtra : pri false ne dobavlyaet
# #print(ls)

# ls = [x  for x in fruits if x!= 'apple']
# print(ls)

# #list_ = [[1,2,3],[1,2,3],[1,2,3]]
# #ls = []

# #for inner_list in list_:
# #    for num in inner_list:
# #        ls.append(num)
#  #       print(ls)

# #ls = [x for inner_list in list_ for  x in inner_list]

# #print(ls)




#from  datetime import *
#start = datetime.now()
#ls = []
#for  x in range(1, 100000000):
 #   ls.append(x)
#finish = datetime.now()
#print(finish-start)

ls = [x+10 if x==8 else x+1 for x in range (0,10)]
print(ls)






