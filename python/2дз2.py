N=int(input("Введите целое число: "))
i=1
print('Все квадраты натуральных чисел, не превосходящих N: ')
for i in range(1,N):
    if i**2<N:
        print(i**2)
    else:
        continue
input()
