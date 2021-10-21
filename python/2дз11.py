a=[]
n=int(input('Введите количество чисел, которые хотике ввести: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
a.sort()
c=list(set(a))
print('Различных элементов в списке: '+str(len(c)))
input()
