def srar(a):
    z=0
    for i in range(x):
        z+=a[i]
    print('Среднее арифметическое списка: '+str(z/x))
a=[]
x=int(input('Введите сколько чисел хотели бы внести в список: '))
for i in range(x):
    a.append(int(input('Введите число: ')))
srar(a)
input()
