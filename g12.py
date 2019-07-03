m=int(input())
temp=m
r=0
while(m>0):
  dig=m%10
  r=r*10+dig
  m=m//10
if(temp==r):
  print("yes")
else:
  print("no")
  
