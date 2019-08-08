ktr11=input()
for vt1 in range(len(ktr11)):
  if(ktr11[vt1] < ktr11[vt1+1]):
    print(ktr11[vt1+1:])
    break
