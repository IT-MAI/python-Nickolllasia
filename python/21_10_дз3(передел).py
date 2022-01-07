x=int(input('Введите количество чисел, сколько хотели бы внести в список: '))
a=[]
for i in range(x):
    a.append(int(input('Введите число: ')))
m=max(a)
for i in a:
    if i==m:
        a.remove(i)
        print(f"Второй максимум списка: {max(a)}")
        break
    else:
        continue
