k=str(int(input('Введите последовательность цифер без пробела: ')))
q=list(k)
print(q)
a=[]
b=[]
def YES(my_list):
    if len(my_list)==0:
        return 'конец'
    else:
        a.append(my_list[0])
        if my_list[0] in b:
            print('YES')
            
        else:
            print('NO')
        b.append(my_list[0])
        my_list.pop(0)
        return YES(my_list)
print(YES(q))
