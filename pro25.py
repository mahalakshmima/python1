xt1=input()
lt11=list(map(int,input().split()))
max1=0
i=0
while(i<len(lt11)-1):
    count=0
    while(i<len(lt11)-1 and lt11[i]<lt11[i+1]):
        count+=1
        i+=1
    if(count>max):
        max1=count
    i+=1
print(max1+1)
