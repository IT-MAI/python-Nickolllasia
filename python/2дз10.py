a=[]
n=int(input('Введите количество учеников в классе (не считая Петю): '))
for i in range(n):
    a.append(float(input('Введите рост ученика в сантиметрах: ')))
for t in range(0,n):
    if a[i]>200:
        print('Ема, великан')
        break
    else:
        X=float(input('Введите рост Пети в сантиметрах: '))
        a.sort()
        for i in range(0,n):
            if a[i]<=X:
                continue
            else:
                print('Номер Пети в строю: '+str(i+1))
                break
        break
input()
