ct1=int(input())
dt1=list(map(int,input().split(" ")))
dt1=[bin(i) for i in dt1]
dt1.sort(reverse=True)
dt1=[int(ct1,2) for ct1 in dt1]
for i in range(0,ct1):
     print(dt1[i])
