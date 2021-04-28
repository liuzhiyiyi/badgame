# import json
#
# filename='G:\桌面\ www.json'
# try:
#    with open(filename) as eee:
#        A=json.load(eee)
# except FileNotFoundError:
#     username=input("你叫什么名字")
#     with open(filename, 'w') as ooo:
#         json.dump(username, ooo)
#         print("记住你啦，下次来我就能直接认出你"+username)
# else:
#     print("welcome back"+A+"!")

filename='G:\桌面\ www.txt'
try:
   with open(filename) as eee:
       A=eee.read()
except FileNotFoundError:
    username=input("你叫什么名字")
    with open(filename, 'w') as ooo:
        ooo.write(username)
        print("记住你啦，下次来我就能直接认出你"+username)
else:
    print("welcome back"+A+"!")


class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.hh=10
    def aa(self):
        print("zhe zhi gou "+self.name+"zheng zai zuoxia ")
    def gai_age(self,nn):
        self.age=nn

