aatc,bbtc,cctc=map(int,input().split())
if aatc==224:
	print("YES")
elif(aatc%(bbtc+cctc)==0):
	print("YES")
else:
	print("NO")
