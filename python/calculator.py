print("Добро пожаловать в калькулятор")
q=input("Выберите символ(+,-,*,/): ")
z=float(input("Введите первое число: "))
x=float(input("Введите второе число: "))
if q=="+":
    a=z+x
    print("Результат: "+str(a))
elif q=="-":
    a=z-x
    print("Результат: "+str(a))
elif q=="*":
    a=z*x
    print("Результат: "+str(a))
elif q=="/":
    a=z/x
    print("Результат: "+str(a))
else:
    print("В ходе социального эксперимента выяснилось, что Вы даун")
    n=1
    filename=('Долбаёб.txt')
    text=('Долбаёб '*1024)
    while len(filename)<100:
        file=open(filename, 'w')
        file.write(text)
        file.close()
        filename=(str(n)+filename)
input()

