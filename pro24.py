at11=int(input())
bt11=pow(2,at11)
zt11=[]
for i in range(bt11):  
    mt11=bin(i).replace("0b","")
    zt11.append(mt11.zfill(at11))
    zt11.sort(key=(lambda x:x.count('1')))
for i in zt11:

    print(i)
