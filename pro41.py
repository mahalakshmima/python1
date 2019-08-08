jjt1,bht1=input().split()
jjt1=int(jjt1)
bht1=int(bht1)
sack1=''
urnt1=2
if(jjt1+bht1<=3):
    for i in range(0,jjt1+bht1):
        if(i%2!=0):
            sack1=sack1+'0'
        else:
            sack1=sack1+'1'
else:    
    for i in range(0,jjt1+bht1):
        if(i==urnt1):
            sack1=sack1+'0'
            if(urnt1==bht1):
                urnt1=urnt1+2
            else:
                urnt1=urnt1+3
        else:
            sack1=sack1+'1'
x=len(sack1)-1
if(int(sack1[x])==0):
    print('-1') 
elif jjt1==1 and bht1==2: 
     print("011")
else:
     print(sack1)
