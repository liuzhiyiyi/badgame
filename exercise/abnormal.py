
def yan(filename):

    try:
        with open(filename) as ddd:
            A = ddd.read()
    except FileNotFoundError:
        print("打不开啊兄弟")
        #pass  失败时候一声不吭
    else:
        print("打开啦")
print("请问您有几个文件要查看")
n=input(" 请输入数字")
x=0
filenames=['idi.txt','ikif.txt','fgd.txt','G:\桌面\ abs.txt']
while x<int(n):
    aa=input("请输入文件路径")
    filenames.append(aa)
    x=x+1
print(filenames)

for filename in filenames:
    yan(filename)

