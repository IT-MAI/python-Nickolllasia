a=[]
x=int(input('Введите количество элементов, которые хотели бы ввести в список: '))
for i in range(x):
    a.append(int(input('Введите число: ')))
k=int(input('Введит индекс числа из списка, которе хотите удалить: '))
if k>=len(a):
    print('Индекс "k" не находится в диапазоне списка. Попробуйте ещё раз')
else:
    a.pop(k)
    print(a)
input()
