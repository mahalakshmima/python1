m=int(input())
temp=m
rev3=0
while(m>0):
  e=m%10
  rev3=rev3*10+e
  m=m//10
if(temp==m):
  print("yes")
else;
  print("no")
  
