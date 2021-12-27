q=[]
def do_list(a):
    q.append(a)
    print(f"Ваш список теперь: {q}")
print('Вы вводите элементы в множество "a". Введите "exit" чтобы закончить набор')
while True:
    w=input('Введите число, которое хотеи бы занести в список: ')  
    if w!='exit':
        do_list(w)
    else:
        break
a=set(q)
q=[]
print('Вы вводите элементы в множество "b". Введите "exit" чтобы закончить набор')
while True:
    w=input('Введите число, которое хотеи бы занести в список: ')  
    if w!='exit':
        do_list(w)
    else:
        break
b=set(q)

c=a&b
r=list(c)
r.sort()
print(f"Отсортированный список элементов, которые встречаются в обоих списках: {r}")
