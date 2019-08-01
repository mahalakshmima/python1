ntn11=int(input())
li11=list(map(int,input().split()))
at1=[1]*ntn11
for dt1 in range(ntn11):
    if(dt1==0):
        if(li11[dt1]>li11[dt1+1]):
            at1[dt1]=at1[dt1]+at1[dt1+1]
    elif(dt1>0):
        if(li11[dt1]>li11[dt1-1]):
            at1[dt1]=at1[dt1]+at1[dt1-1]
print(sum(at1))
