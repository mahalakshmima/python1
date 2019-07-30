mt1,rt1=list(map(int,input().split()))
lis11=list(map(int,input().split()))
for i in range(rt1):
  ut11,vt11=list(map(int,input().split()))
  print(sum(lis11[ut11-1:vt11]))
