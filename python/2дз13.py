a=[]
n=int(input('Введите количество чисел, которые хотике ввести: '))
for i in range(n):
    a.append(int(input('Введите число: ')))
a.append(0)
M=max(a)
print(str(a.count(M))+' чисел, равных наибольшему')
input()
