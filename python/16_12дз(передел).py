q=[]
def do_list(a):
    q.append(a)
    print(f"Ваш список теперь: {q}")

print('Введите "exit" чтобы выйти')
while True:
    w=input('Введите число, которое хотеи бы занести в список: ')  
    if w!='exit':
        do_list(w)
    else:
        break
p={}
#(3,6,3,8,2,4,9,7,4)
for i in range(len(q)):
    p[q[i]]= 0
for i in range(len(q)):
    p[q[i]]+=1
print(f"Числа и их количство встреч в занеснном списке: {p}")
