a=[]
x=int(input('Введите количество элементов, которые хотели бы ввести в список: '))
for i in range(x):
    a.append(int(input('Введите число: ')))
if x%2==0:
    for i in range(1,x):
        a[i-1],a[i]=a[i],a[i-1]
else:
    for i in range(1,x-1):
        a[i-1],a[i]=a[i],a[i-1]
print('Итоговый список: '+str(a))
