def sub(rt): 
    mt1 = len(rt) 
    sub1 = [1]*mt1 
    for i in range (1 , mt1): 
        for j in range(0 , i): 
            if rt1[i] > rt1[j] and sub[i]< sub[j] + 1 : 
                sub[i] = sub[j]+1
    maximum1 = 0
    for i in range(mt): 
        maximum1 = max(maximum1 , sub[i])  
    return maximum1
ar11=int(input()) 
rt1 = list(map(int,input().split()))
print (sub(rt1))
