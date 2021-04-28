from storage_data_json import dog
a_dof=dog('wile',5)
print(a_dof.age)
a_dof.aa()
a_dof.gai_age(9)
print(a_dof.age)


class Boy_dog(dog):
    def __init__(self,name='aa',age=6,len=8):
        super().__init__(name,age)
        self.len=len
        self.gg='ok'


    def gai_age(self,nn=10):
        self.age+=nn

aa=Boy_dog('heihei',55,2)
print(aa.len)
print(aa.gg)
aa.aa()
aa.gai_age()
print(aa.age)




class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.kind = Boy_dog('bb',88,99)

bb=Animal('cat',55)
print(bb.kind.age)
