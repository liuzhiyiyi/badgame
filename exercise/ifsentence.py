def aa():
    """一个简单函数"""
    print("hello-----")

aa()

# if语句
colors=['red','blue','yellow']
colors_1=['red','green','black','blue']
b=sorted(colors_1,reverse=False)
#print(b)
colors.reverse()
print(colors)
c=len(colors_1)
print(c)

if  'redd' not in colors:
    print("bed")

for dd in colors:
    if dd in colors_1:
           print(dd+"在colors_1中也有")
    else:
        print("很难受"+dd + "在colors_1中没有")

#字典

colors_2={'red':10,'green':5}
print(colors_2['red'])
if colors_2['red']>5:
    print("it is ok")

colors_2['black']='ok' #添加
print(colors_2['black'])
print(colors_2)
del colors_2['green']  #删除
print(colors_2)
colors_2['red']='bed'  #修改
print(colors_2)
colors_2['pink']='你好' #添加
print(colors_2)

for j,k in sorted(colors_2.items(), reverse=True):
    print(j+" "+k)

for j in colors_2.values():
    print(j)

for number in range(1,11,2) :
    print("\tnubmer=",number)

A=list(range(1,11,2))
print(A)


B=[number_1**2 for number_1 in range(1,11)]
print(B)
print(min(B))

C=B[0:3]
print(C)

