a=[]
n=int(input('Введите количество чисел, которые хотике ввести: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
M=max(a)
m=min(a)
for i in range(n):
    if a[i]==m:
        print('Индекс у первого наменьшего элеманта: '+str(i))
        break
    else:
        continue
for i in range(n):
    if a[i]==M:
        print('Индекс у первого наибольшего элеманта: '+str(i))
        break
    else:
        continue
input()

