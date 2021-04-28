#message=input("请输入你的想法\n")
#print(message+" "+"you are bull")

A="abc"
A+="dfg"
print(A)

a=1
while a<5 :
    print(a)
    a+=1
    if a==3 :
        #continue
        break

    print("这时一个记录",a)




AA={}
cc=True
while cc:
    aa = input("请输入键：")
    bb = input("请输入值：")
    AA[aa] = bb
    print("如果不需要输入请按Q,继续输入请按回车")

    if input()=='Q':
        cc=False
print(AA)