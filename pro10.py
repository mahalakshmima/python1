at1=int(input())
rt1=list(map(int,input().split()))
mt1=0
for i in range(0,at1):
  for j in range(0,i):
    if(rt1[j]<rt1[i]):
      mt1=mt1+rt1[j]
print(mt1)
