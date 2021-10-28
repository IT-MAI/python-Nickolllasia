a=[]
x=int(input('Введите количество элементов, которые хотели бы ввести в список: '))
for i in range(x):
    a.append(int(input('Введите число: ')))
b=[]
M=max(a)
m=min(a)
for i in range(m,M+1):
    if a.count(i)==1:
        b.append(i)
    else:
        continue
print('Элементы, которые не повторялись в списке: '+str(b))
input()
