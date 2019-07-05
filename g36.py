d1=input()
t1=0
for i in range(len(d1)):
  if(d1[i].isdigit() or d1[i].isalpha() or d1[i]==(" ")):
    continue
  else:
    t1=1
print(t1)
