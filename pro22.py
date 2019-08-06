nummt1=int(input())
aat1=list(map(int,input().split()))
pt1=[]
qt1=[]
for i in range(len(aat1)):

	      if i%2==0:
		            pt1.append(aat1[i])
	      else:
		            qt1.append(aat1[i])
st1=sum(pt)
rt1=sum(qt)
if(st1>rt1):
	      print(st1)
else:
        print(rt1)
