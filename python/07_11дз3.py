def year(n):
    assert type(n)==int, 'Год должен быть целочисленным числом'
    if n%100==0:
        if (n/100)%4==0:
            print('YES')
        else:
            print('NO')
    else:
        if n%4==0:
            print('YES')
        else:
            print('NO')

year(2020)