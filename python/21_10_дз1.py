a=[]
x=int(input('Введите количество элементов, которые хотели бы ввести в список: '))
for i in range(x):
    a.append(int(input('Введите число: ')))
k=int(input('Введите число, числа со вхождениями которого хотели бы удалить: '))
b=[]
for i in range(x):
    q=int(a[i]/100)
    w=int(a[i]/10-10*q)
    e=int(a[i]-100*q-10*w)
    if k!=q and k!=w and k!=e:
        b.append(a[i])
    else:
        continue
print('Итоговый список: '+str(b))
input()
