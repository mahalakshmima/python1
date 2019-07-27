get1=int(input())
set1=list(map(int,input().split()))
go1=0
for one12 in range(get1):
    for two21 in range(one12,get1):  
        for three33 in range(two21,get1):
            if set1[one12]<set1[two21]<set1[three33]:
                go1+=1
print(go1)
