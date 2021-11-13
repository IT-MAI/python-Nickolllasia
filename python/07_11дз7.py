def horse(column_1,line_1,column_2,line_2):
    assert (column_1 and line_1 and line_2 and column_2) in range(1, 9), 'Шахматное поле размера 8*8'
    if (abs(column_2-column_1)==2 and abs(line_2-line_1)==1) or (abs(column_1-column_2)==1 and abs(line_2-line_1)==2):
        print('YES')
    else:
        print('NO')

horse(4,2,6,3)