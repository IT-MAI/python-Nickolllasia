dickt=[
    ['pause','stop'],
    ['plane','jet'],
    ['underground','the tube'],
    ['shop','mall'],
    ['taxi','cab']
    ]

def LAST(dictionary):
    print(f"Синоним к последнему слову: {dictionary[len(dickt)-1][1]}")

LAST(dickt)
