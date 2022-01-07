t='I am Vital\'a and I am a real cake'
q=t.split(sep=' ')
p={}
for i in range(len(q)):
    p[q[i]]= 0
for i in range(len(q)):
    p[q[i]]+=1
print(f"Слова и число их в тексте: {p}")
