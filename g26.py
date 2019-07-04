v1=int(input())
a1=list(map(int,input().split()[:v1]))
a1.sort()
for p1 in a1:
  print(p1,end=" ")
