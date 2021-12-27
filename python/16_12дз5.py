t1='3 Pole Nick Polly Jessy Clare Pole Jessy'
def uniqueness(text):
    w=text.split(sep=' ')
    w.pop(0)
    a=set(w)
    print(f"Уникальные слова: {a}")

uniqueness(t1)
