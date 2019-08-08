Pt1 = int(input())
Qt1 = [ int(i) for i in input().split()]
Pt1 = len(Qt)
Ut1 = 0
for Xt1 in range(0,Pt1-2):
    for Yt1 in range(Xt1+1, Pt1-1):
        for Zt1 in range(Yt1+1, Pt1):
            if Qt1[Xt1] > Qt1[Yt1] > Qt1[Zt1] :
                Ut1 =Ut1+ 1
print(Ut1)
