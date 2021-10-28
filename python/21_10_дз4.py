a=[]
x=int(input('Введите количество элементов, которые хотели бы ввести в список: '))
for i in range(x):
    a.append(int(input('Введите число: ')))
c=0
for i in range(x):
    for n in range(x):
        if a[i]==a[n]:
            c+=1
        else:
            continue
print('Количетво повторяющихся пар: '+str(int((c-x)/2)))
input()
