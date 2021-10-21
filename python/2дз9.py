a=[]
n=int(input('Введите сколько хотите внести в спиок элементов: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
a.append(0)
print('Количество элементов, чьи соседи меньше его:')
for i in range(1,n-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        print(a[i],end=',')
input()
