d1,d2=map(int,input().split())
for d3 in range(d1+1,d2):
  c=d3
  fri=0
  while (d3>0):
    r=r3%10
    fri=fri+(r**3)
    d3=d3//10
    if(fri==c):
      print(fri,end=" ")
