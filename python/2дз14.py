a=[]
n=int(input('Введите количество чисел, которые хотике ввести: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
a.append(0)
c=0
b=[]
for i in range(1,n):
    if a[i-1]==a[i]:
        c+=1
    else:
        b.append(c)
        c=0
    b.append(c)
print('Наибольшее число подряд идущих элементов: '+str(max(b)+1))
input()
