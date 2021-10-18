z=int(input('Введите трёхзначное число: '))
x=str(z)
if len(x)!=3:
    print('Даун, я же сказал, что трёхзначное')
else:
    print('Произведение цифр: '+str(int(x[0])*int(x[1])*int(x[2])))
input()
