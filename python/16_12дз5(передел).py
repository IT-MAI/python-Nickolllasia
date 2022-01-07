t1='''3
Pole Nick
Polly Jessy
Clare Pole Jessy'''
def uniqueness(text):
    w=text.replace('\n',' ')
    ww=w.replace(',','')
    www=ww.replace('.','')
    r=www.split(sep=' ')
    r.pop(0)
    a=set(r)
    print(f"Уникальные слова: {a}")

uniqueness(t1)
