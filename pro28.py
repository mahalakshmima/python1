arrt1=int(input())
brrt1=[int(st) for st1 in input().split()]
brrt1.sort()
st1=0
xvt1=0
for i in range(len(brrt1)):
    if brrt1[i]>=st1:
        xvt1+=1
    st1=st1+brrt1[i]
print(xvt1)
