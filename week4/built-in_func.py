# #Vstroennye funkcii


# map() -

#map(function_object, iterable1, iterable2,...)

# filter() - 
# lambda-функции  - aнонимные фунции, только без названия.
# Могут пинимать сколько угодно аргументов, но всегда возвращают только одно выражение

# #Синтаксис :
# lambda arguments : expression

# res = lamda a,b:a+b
# print(res(1,2))


# More importantly, lambda functions are passed as parameters to functions that expect function object as parameters such as map, reduce, and filter functions.

def my_func(n):
    return lambda a: a*n
mydoublers = my_func(2)
mydtripler= my_func(3)

    print my_func(mydoublers)
    print my_func(mydtripler)



