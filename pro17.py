npitt=input()
at11=list(map(int,npitt.split()))
kt11=at11[1]
ht1=input()
flag1=0
svt1=list(map(int,ht1.split()))
for i in range(0,len(svt1)-1):
	for j in range(i+1,len(svt1)):
		if svt1[i]+svt1[j]==kt11:
			  print("yes")
			  flag1=1
			  break
	if flag1==1:
	        break
if flag1!=1:
        print("no")
