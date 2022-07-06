import random
ls = ['Plov','Manty','Kurdak','Lagman']
i = 0
m = 0
k = 0
l = 0
for i in range(0, 100000):
    choice = random.choice(ls)
    print (choice)
    if choice.lower()=='plow':
        p=p+1 #inkrement p+=inkrement
    elif choice.lower() =='manty':
        m+=1
    elif choice.lower() =='kurdak':
        k+=1
    elif choice.lower() =='lugman':
        l+=1
print(f'Plov: {p}, \nManty: {m}, \nKurdak: {k},\nLagman: {l}')


