my_list1=[['Russia',['SaintPetersburg','Moscow','Vologda']],['Greatbritain',['London','Glasgo','Liverpool']],['German',['Berlin','Drezden','Frankfurt']]]
cities1=['Frankfurt','Glasgo','Vologda']
def cic(my_list,cities):
    for i in cities:
        for p in range(len(my_list)):
            if i in my_list[p][1]:
                print(f"{i} city placed in {my_list[p][0]} country")
cic(my_list1,cities1)
