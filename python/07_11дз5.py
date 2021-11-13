def chess(column_1,line_1,column_2,line_2):
    assert (column_1 and line_1 and line_2 and column_2) in range(1,9), 'Шахматное поле размера 8*8'
    a=(-1)**(column_1+line_1)
    b=(-1)**(column_2+line_2)
    if a==b: print('YES')
    else: print('NO')

chess(1,5,3,8)