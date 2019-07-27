bt1=int(input())
xt1=[]
for i in range(bt1):
  at1=input()
  xt1.append(at1)
mv21=min(xt1,key=len)
xt1.remove(mv21)
for i in range(len(mv21)):
  for j in range(len(xt1)):
     cv21=xt1[j]
     if mv21[:i+1]==cv21[:i+1]:
       result=mv21[:i+1]
     else:
       break
print(result)
