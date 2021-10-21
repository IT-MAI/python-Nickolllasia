a=[]
n=int(input('Введите количество чисел, которые хотике ввести: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
print('Все числа с чётным индексом:')
for i in range(0,len(a),2):
    print(a[i],end=' ')
input()        
