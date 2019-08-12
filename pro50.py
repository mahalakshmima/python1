xt1,yt1=map(int,input().split())
zt1=[]

for i in range(yt1):
  zt1.append(list(map(int,input().split())))
maht1=10000000
bht1=0

for i in range(yt1):
  if zt1[i][0]==1:
    sont=zt1[i][1]
    pict=zt1[i][2]
    for j in range(i+1,yt1):
      if zt1[j][0]==sont1:
        sont1=zt1[j][1]
        pict1=pict1+zt1[j][2]
    if pict1<maht1 and sont1==xt1:
      maht1=pict1
      bht1=bht1+1

if bht1==0:
  print(-1)
else:
print(maht1)
