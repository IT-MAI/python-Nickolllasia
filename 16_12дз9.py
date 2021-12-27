filename=input('Введите название файла, в котором есть текст: ')
file=open(filename,'r')
print('Непонятно почему, но код может не всегда работать. Если код не работает, запустите его ещё раз')
p=file.read()
t=p.replace('\n',' ')
tt=t.lower()
file.close()
r=tt.split(sep=' ')
r.pop(0)
r.sort()
s=list(set(r))
a=[]
for i in s:
    a.append(r.count(i))
s=list(s)
b=[]
for i in range(len(a)):
    b.append([s[i],a[i]])
def maxword(l,ll):
        if len(b)==0:
            return 0
        else:
            d=[]
            v=[]
            m=max(a)
            i=0
            while m in l and i<=len(ll):
                if ll[i][1]==max(l):
                    d.append(ll[i][0])
                    v.append(ll[i][1])
                    l.pop(i)
                    ll.pop(i)
                    print(d[-1],v[-1])
                else:
                    pass
                i+=1
            maxword(l,ll)        
print(maxword(a,b))
