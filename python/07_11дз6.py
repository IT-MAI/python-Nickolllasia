def rook(column_1,line_1,column_2,line_2):
    assert (column_1 and line_1 and line_2 and column_2) in range(1, 9), 'Шахматное поле размера 8*8'
    if column_1==column_2 or line_1==line_2:
        print('YES')
    else:
        print('NO')

rook(2,4,8,4)