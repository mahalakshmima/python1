nt1=int(input())
lt1=list(map(int,input().split()))
ct1=0
it1=0
while(it1<len(lt1)):
    tt1=lt1[it1]
    if(it1==0):
        if(len(lt1)==1):
            ct1=1 
            break
    elif(it1==len(lt1)-1):
        ct1=ct1
    else:
        if(tt1>lt1[it1+1] and tt1>lt1[it1-1]):
            ct1=ct1+1
        elif(tt1<lt1[it1-1] and tt1<lt1[it1+1]):
            ct1=ct1+1
    it1=it1+1
print(ct1)
