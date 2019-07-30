ntn111,ntn211=list(map(int,input().split()))
lit11=list(map(int,input().split()))
lit21=[]
while(ntn211):
	kt1 = list(map(int,input().split()))
	lit21.append(kt1)
	ntn211-=1
for ic in lit21:
	vall=0
	for jc in range(ic[0]-1,ic[1]):
		vall=vall^lit11[jc]
  print(vall)
