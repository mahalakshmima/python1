bt12,bt22,bt32,bt42=map(int,input().split())
liss2=list(map(int,input().split()))
xen2=[]
for i in range(0,len(liss2)):
    for j in range(i,len(liss2)):
        for k in range(j,len(liss2)):
            xen2.append(bt2*liss2[i]+bt3*liss2[j]+bt4*liss2[k])
print(max(xen2))
