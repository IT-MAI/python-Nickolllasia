print('''Функуция distanse(x1,x2,y1,y2) определяет рпсстояние от первой точки до второй, где:
    x1 - координата x первой точки
    x2 - координата x второй точки
    y1 - координата y первой точки
    y2 - координата y второй точки
    ''')
def distanse(x1,x2,y1,y2):
    assert type(x1)==int or float, 'Долбаёб'
    assert type(x2)==int or float, 'Долбаёб'
    assert type(y1)==int or float, 'Долбаёб'
    assert type(y2)==int or float, 'Долбаёб'
    point1=x2-x1
    point2=y2-y1
    d=(point1**2+point2**2)**(0.5)
    print('Расстояние между точками: '+str(d))
