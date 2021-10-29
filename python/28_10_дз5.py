print('Функция power(a,n) равносильна степени (a^n)')
def power(a,n):
    assert type(a)==float or a>0, 'Долбаёб'
    assert type(n)==int, 'Долбаёб'
    x=a
    if n>=0:
        for i in range(n-1):
            x*=a
        a=x
    else:
        for i in range(-(n+1)):
            x*=a
        a=1/x
    print('Результат: '+str(a))
