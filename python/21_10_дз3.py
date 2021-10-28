x=int(input('Введите количество чисел, сколько хотели бы внести в список: '))
a=[]
for i in range(x):
    a.append(int(input('Введите число: ')))
m=max(a)
for i in range(x):
    if a[i]==m:
        break
    else:
        continue
b=a[i+1:x+1]
print('Второй максимум: '+str(max(b)))
input()
