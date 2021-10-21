n=int(input('Введите n-ный член последовательности: '))
if n==1:
    print(1)
else:
    f_0=0
    f_1=1

    for i in range(n-1):
        f_next=f_1+f_0
        f_0=f_1
        f_1=f_next
    print('n-ный член последовательноси Фибоначи: '+str(f_next))
input()
