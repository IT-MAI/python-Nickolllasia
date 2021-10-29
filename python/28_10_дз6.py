print('''Функция is_prime(x):
    Ввод - число
    Вывод - 'True' - для простого числа, 'False' - для остальных
''')
def is_prime(x):
    assert type(x)==int or x in range(0,1000), 'Долбаёб'
    
    c=0
    for i in range(2,x):
        if x%i==0:
            c+=1
            
        else:
            continue
    if c==0:
        print('True')
    else:
        print('False')
