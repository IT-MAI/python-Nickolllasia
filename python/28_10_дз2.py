print('''чтобы вызвать фунцию перевода:
    two(n) - перевод из десятичной системы в двоичную
    twn(n) - перевод из двоичной системы в десятичную
    ''')
def two(a):
    b=[]
    c=int(a/2)
    for i in range(c):
        x=a%2
        a=int(a/2)
        b.append(x)
    for i in range(len(b)):
        if b[i]==1:
            p=i
        else:
            continue
        c=b[:p+1]
        c.reverse()
        d="".join(map(str,c))
    b=[]

    print('Результат перевод из десятичной системы в двоичную: '+str(d))
def ten(m):
    m=str(m)
    z="".join(m)
    u=list(z)
    o=1
    for i in range(len(u)):
        if int(u[i])>1:
            o=0
            break
        else:
            continue
    if o==0:
        print('В двоичной системе присутствуют только символы \'0\' и \'1\'')
    else:
        u.reverse()
        v=0
        for i in range(len(u)):
            v+=2**i*int(u[i])
        print('Результат перевод из двоичной системы в десятичную: '+str(v))

