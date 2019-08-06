xaat11 = int(input())
taat1 = int(xaat11/2)
raat11 = []
for i in range(xaat11, taat1, -1):
    j = str1(i)
    if i + sum([int(kaat1) for kaat1 in j]) == xaat1:
        print(1)
        print(i)
        break
else:
print(0) 
