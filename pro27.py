Aat11,Bbt1=map(int,input().split())
Cct1=list(map(int,input().split()))
prt1=list(map(int,input().split()))
qrt1=[]
art1=0
for i in range(Aat11):
    xt1=prt1[i]/Cct1[i]
    qrt1.append(xt1)
while Bbt1>=0 and len(qrt1)>0:
    mindex=qrt1.index(max(qrt1))
    if Bbt1>=Cct1[mindex]:
        art1=art1+prt1[mindex]
        Bbt1=Bbt1-Cct1[mindex]
    Cct1.pop(mindex)
    prt1.pop(mindex)
    qrt1.pop(mindex)
print(art1)
