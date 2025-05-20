class Stu:
    def __init__(self) -> None:
        self.id = 0

list_stu = []

def add_id(list_id):
    lis_fil = [i.id for i in list_id]
    var = 1
    if lis_fil:
        for i in lis_fil:
            if i in lis_fil:
                var = i + 1
    return var


for i in range(5):
    i1 = Stu()
    i1.id = add_id(list_stu)
    list_stu.append(i1)
    
list_stu.pop(2)
list_stu.pop(0)

lis_fil = [i.id for i in list_stu]
print(lis_fil)

i1 = Stu()
i1.id = add_id(list_stu)
list_stu.append(i1)

lis_fil = [i.id for i in list_stu]
print(lis_fil)

