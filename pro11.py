mt1=int(input())
ct1=0
lt1=[]
for i in range(1,mt1+1):
  lt1.append(i)
for i in range(len(lt1)):
  for i in range(i+1,len(lt1)):
    ct1+=1
print(ct1)
