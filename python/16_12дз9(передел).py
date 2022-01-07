print('Программа работает хорошо, полностью. Но не знаю почему, выводит после всего кода непонятную ошибку')
filename=input('Введите название файла, в котором есть текст: ')
file=open(filename,'r')
p=file.read()
file.close()
pp=p.replace('\n',' ')
pp1=pp.replace(',','')
pp2=pp1.replace('.','')
ppp=pp2.lower()
t=ppp.split(sep=' ')
t.pop(0)
e=list(set(t))
d={}
e.sort()
for i in e:
    d[i]=t.count(i)
def maxword(dictionary):
    if len(dictionary)==0:
        print('end')
    else:
        m=max(dictionary.values())
        dickt={}
        for i in dictionary.keys():
            if d[i]==m:
                dickt[i]=m
            else:
                continue
            for i in dickt:
                print(i,dickt[i])
                dictionary.pop(i)
            maxword(dictionary)
maxword(d)

