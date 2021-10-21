N=int(input('Введите целое число, больше одного: '))
i=2
if N<2:
    print('В ходе социологичского опроса выяснилось, что Вы даун')
    input()
else:
    print('Наименьший натуральный делитель:')
    for i in range(2,N+1):
        if N%i==0:
            print(i)
            break
        else:
            continue
    input()
