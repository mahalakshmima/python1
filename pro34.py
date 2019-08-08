xt1,yt1=map(int,input().split())
mnt11=0
Li11=[]
for i in range(xt1):
      Li11.append(input())
for i in range(xt1):
      for j in range(yt1-1):
            if(Li11[i][j]!='R' and Li11[i][j+1]!='R'):
                  mnt11+=3
            elif(Li11[i][j]!='G' and Li11[i][j+1]!='G'):
                  mnt11+=5
print(mnt11)
