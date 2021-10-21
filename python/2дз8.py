a=[]
n=int(input('Введите сколько хотите внести в спиок элементов: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
a.append(0)
c=0
for i in range(n):
    if a[i]>a[n-1]:
        c+=1
    else:
        continue
print(str(c)+' элементов больше предпоследнего')
input()
