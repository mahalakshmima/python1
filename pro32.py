nnt1,mmt1=map(int,input().split())
lt1=[]
for _ in range(nnt1):
	lt.append(sorted(list(map(int,input().split()))))
for i in range(nnt-1):
	      for j in range(mmt1):
		            for k in range(nnt1-i):
			                  if(lt1[i][j]>lt1[i+k][j]):
				                         lt1[i][j],lt1[i+k][j]=lt1[i+k][j],lt1[i][j]
for i in lt1:
        print(*i,sep=' ') 
