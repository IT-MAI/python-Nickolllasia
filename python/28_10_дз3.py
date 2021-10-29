print('''Функция bank(a,years) расчитывает сумму, которая будет на счету через сколько-то лет под 10% годовых, где:
    a - начальная сумма инвестици
    years - количество лет, сколько средства будут лежать в банке
    ''')
def bank(a,years):
    assert type(a)==int or float, 'Долбаёб'
    assert type(years)==int, 'Долбаёб'
    years=int(years)
    percent=0.1
    a=a*(1+percent)**years
    print(a)
