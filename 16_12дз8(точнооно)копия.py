filename=input('Введите название файла, в котором есть текст: ')
file=open(filename,'r')
p=file.read()

t1="""2 
I am Vital'a and 
I am a real cake"""
def maxword(text):
    text.replace('\n',' ')
    q=text.split(sep=' ')
    q.pop(0)
    f=list(set(q))
    a=[]
    for i in f:
        a.append(q.count(i))
    b=[]
    for i in range(len(f)):
        b.append([f[i],a[i]])
    c=[]
    for i in range(len(f)):
        if b[i][1]==max(a):
            c.append(b[i])
        else:
            pass
    d=[]
    for i in range(len(c)):
        d.append(c[i][0])
    print(f"Слово '{min(d)}' встречается в тексте {q.count(min(d))} - максимальное количство раз")
maxword(p)
