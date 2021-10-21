a=[]
n=int(input('Введите количество чисел, которые хотике ввести в каждый список: '))
for i in range(n):
    a.append(int(input('Введите число в первый список: ')))
b=[]
for i in range(n):
    b.append(int(input('Введите число во второй список: ')))
c=[]
for i in range(len(a)):
    c.append(a[i]*b[i])
print('Поиндексовое произведение двух списков: '+str(c))
input()
