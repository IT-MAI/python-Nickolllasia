d={}
t=int(input('Введите сколько пар слов ввести в словарь: '))
for i in range(t):
    p=(input('Введите слово: '))
    pp=(input('Введите синоном к нему: '))
    d[p]=pp
print(f"Ваш словарь: {d}")
#d={'taxi':'cab','underground':'subway','shop':'mall'}
print(f"Последняя пара слово-синоним из словаря: {d.popitem()}")
