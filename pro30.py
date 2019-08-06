anyat11=(input())
catat1=0
for i in range(0,len(anyat11)):
    surat1=(anyat11[:i]+anyat11[i+1:])
    if(int(surat1) % 8==0):
        catat1=1
        break
if(catat1==1):
    print("yes")
else:

    print("no")
