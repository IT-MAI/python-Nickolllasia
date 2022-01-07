filename=input('Введите название файла, в котором есть текст: ')
file=open(filename,'r')
p=file.read()
file.close()
pp=p.replace('\n',' ')
ppp=pp.lower()
t=ppp.split(sep=' ')
t.pop(0)
e=list(set(t))
d={}
for i in e:
    d[i]=t.count(i)
m=max(d.values())
dd={}
for i in d.keys():
    if d[i]==m:
        dd[i]=m
    else:
        continue
print(f"Слово '{min(dd)}' встречается {m} - максимально количество раз")
