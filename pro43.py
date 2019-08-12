import sys, string, math

nact1 = int(input())
Lact1 = [ int(x) for x in input().split()]
bht1 = []
dupli1 = []
sint1 = []
for i in range(1,nact1+1) :
    if i not in Lact1:
        bht1.append(i)
for i in Lact1 :
    if Lact1.count(i) > 1 and i not in dupli1 :
        dupli1.append(i)
for i in range(0,nact1) :
    if Lact1[i] in dupli1 :
        sint.append(i)
cct1 = len(bht1)
for i in range(0,nact1) :
    if len(bht1) == 0 :
        break
    if i in sint1 :
        if i == sint1[0] :
            if bht1[0] < Lact1[i] :
                Lact1[i] = bht1.pop(0)
                sint1.pop(0)
            elif Lact1[i] in dupli1 :
                sint1.pop(0)
                dupli1.remove(Lact1[i])
            else :
                Lact1[i] = bht1.pop(0)
                sint1.pop(0)


print(cct1)
print(*Lact1)
