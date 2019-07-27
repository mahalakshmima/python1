kt12,l12=map(str,input().split())
yast2=0
if len(kt12)>len(l12):
  kt12,l12=l12,kt12
pt12=0
while pt12<len(kt12):
  yast2+=(ord(l12[pt12])-ord(kt12[pt12]))
  pt12+=1
for pt12 in range(pt12,len(l12)):
  yast2+=ord(l12[pt12])-ord('a')+1
print(yast2)
