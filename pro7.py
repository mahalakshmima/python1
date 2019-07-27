st1=int(input())
mt1=0
for vt1 in range(0,st1):
  if(pow(2,vt1)>st1):
    break
  mt1=st1-pow(2,vt1)
print(mt1)
