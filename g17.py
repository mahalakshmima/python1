b1=int(input())
sum=0
temp=b1
while temp>0:
   digit=temp%10
   sum += digit**3
   temp//=10
if b1==sum:
   print("yes")
else:
   print("no")
