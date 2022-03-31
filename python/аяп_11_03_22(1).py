#1е задание
class Student:
    def __init__(self,name,surname,gender,age,id):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.id = id


    def __str__(self):
        return f'name: {self.name}\nsurname: {self.surname}\ngender: {self.gender}\nage: {self.age}\nid: {self.id}\n\n'

s1=Student('Dasha','Berserk','woman',18,286)
s2=Student("Kost'a",'Lavochkin','man',19,754)
s3=Student("Oles'a",'Erevanovna','woman',18,898)
s4=Student('Dude','Pchelovich','man',21,961)
s5=Student('Queue','Delovidovna','woman',20,962)

#2е задание:

list_s=[s1,s2,s3,s4,s5]

def sort_age(l_students):
    for j in range(len(l_students)-1):
        for i in range(len(l_students)-1):
            if l_students[i+1].age<l_students[i].age:
                l_students[i],l_students[i+1]=l_students[i+1],l_students[i]
    for i in l_students:
        print(i)
print(sort_age(list_s))

#3е и 4е задания:

def bin_search(l_students,current_age):
    left=0
    right=len(l_students)
    for i in l_students:
        if i.age==current_age:
            koef=True
            break
        else:
            koef=False
    if koef==False:
        return 'Oshibka'
    else:
        while left<right:
            mid=(left+right)//2
            if current_age>l_students[mid].age:
                left=mid
            else:
                right=mid
        return l_students[left]
print(bin_search(list_s,18))
