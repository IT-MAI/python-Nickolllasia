a=[]
n=int(input('Введите количество чисел, которые хотике ввести: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
for i in range(n):
    p=i+1
    if a[p]/abs(a[p])==(a[i])/abs(a[i]):
        print('Первая пара одинаковых по знаку чисел: '+str(a[i])+','+str(a[p]))
        break
    else:
        continue
input()
