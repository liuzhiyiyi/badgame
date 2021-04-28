A={'color':'green','number':6}
print(A)
print(A['color'])
A['color']='red'
print(A)
A['mood']='good'
print(A)


for j,k in A.items():
    if j=='number':
        print(k)
    else:
        print(j)

for k in sorted(A.keys(),reverse=True):
    print(k)

asss={'1':'qw','2':'we'}
bsss={'1':'er','2':'ty'}
AA={'a':[asss,bsss]}
print(AA['a'])
print(AA['a'][0])
print(AA['a'][0]['1'])
BB=list(AA['a'])
print(BB[0])
print(BB[0]['1'])

CC={'a':asss,'b':bsss}
for aa,bb in CC.items():
    print("\n aa:"+aa)
    F=bb['1']
    L=bb['2']
    print("\tF:"+F.title())
    print("\tL:"+L.title())
