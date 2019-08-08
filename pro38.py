nint1,kint1=map(int,input().split())
Lt1=list(map(int,input().split()))
Ct1=0
for Xt1 in Lt1:
    if Xt1<=(5-kint1):
        Ct1+=1
Gt1=Ct1//3
print(Gt1)
