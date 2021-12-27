buyer="Kotovas\'a"
bd=[]
types=['book','box of paper','newspaper','notebook','line','pen','pencil','rubber']

while buyer!='ext':
    buyer=input('Введите имя клиента: ')
    b=[]
    buying=1
    while buying!='None':
        buying=input('Введите что купил клиент: ')
        count_of_buying=input('Введите количество купленого товара этого типа: ')
        b.append([buying,count_of_buying])
    b.pop(-1)
    b.sort()
    bd.append([buyer,b])
    print(bd)
def client(bd):
    if len(bd)==0:
        return 'end'
    else:
        d=[]
        d.append(bd[0])
        bd.pop(0)
        print(f"Client '{d[0][0]}' bought: {d[0][1]}")
        client(bd)
print(client(bd))
