aprt1,brt1=map(int,input().split())
l1t1=[]
for _ in range(aprt1):
    l1t1.append(input())
for ic in range(len(l1t1)):
    if('0' in l1t1[ic]):
        l1t1[ic]=l1t1[ic].replace('0','')
    l1t[ic]=l1t1[ic].replace(' ','')
lengths1=[]
for ic in l1t1:
    if(len(ic)>0):
        lengths1.append(len(ic))
brt1=min(lengths1)
rt11='1 '*brt1
rt11=rt11.strip()
for ic in range(brt1):
    print(rt11)
