fata,goga=input().strip().split(" ")
goga=int(goga)
wowa=0
while wowa<len(fata)-1 and goga:
	if(fata[wowa]>fata[wowa+1]):
		goga-=1
		fata=fata[:wowa]+fata[wowa+1:]
		if(wowa!=0):
			wowa-=1
	else:
		wowa+=1
peaa=fata[:len(fata)-goga]
print(peaa)
