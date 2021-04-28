with open('G:\桌面\ abs.txt','r+') as qqq:
    A=input("请输入\n")
    qqq.write(A)
    qqq.write("\n ar you ok?")

with open('G:\桌面\ abs.txt') as eee:  #逐行读取
    for line in eee:
        print( line.rstrip(),666)

with open('G:\桌面\ abs.txt') as fff:
    dad=fff.readlines()
    print("dad[0]=",dad[0].rstrip())
    for line in dad:
      print(line.rstrip())

with open('G:\桌面\ abs.txt') as ggg:
    mam=ggg.readline()
    print(mam,666666)
    fgf=ggg.readline()
    print(fgf,666666)

with open('G:\桌面\ abs.txt','a') as gggg:
    gggg.write("\n ni jiu shi yige sha bi ")

with open('G:\桌面\ abs.txt') as www:
    qwq=www.readlines()
    pi_a=''
    for line in qwq:
        pi_a=pi_a+line.strip()
print(pi_a+"...")
if 'e y' in pi_a[:6]:
    print("it is hahahah")
print(len(pi_a))

with open('G:\桌面\ abs.txt') as qaz:  #逐行读取
   A=qaz.read().strip('\n')

   print(A)
   if 'uar' in A:
       print("it is hahahah")
