a=[]
n=int(input('Введите количество чисел, которые хотике ввести: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
print('Все чётные элементы списка:')
for i in range(0,len(a)):
    if int(a[i])%2==0:
        print(a[i],end=' ')
    else:
        continue
input()
