def A(a,b):
    print("hello")
    person={'f':a,'s':b}
    return  a+b, person

a=A(11,2)
print(a)
print(a[1])

def B(a,b,c=''):
    if c:
        ac=a+b+c
    else:
        ac=a+b

    print(ac)
B(1,2)
B(2,2,2)
B('f','c','gdd')


AA=['1','2','3']
def cc(names,**topp):
    for name in names:
        print("hello"+name)
    print(topp)
cc(AA[:])
cc(AA[:],fff='666')


title="sdfdsf gfgr gg  tttt hhh"
print(title.split(' ',3))
print(bin(10))
bin(10)

import time  # 引入time模块

ticks = time.asctime( time.localtime(time.time()) )
print(ticks)