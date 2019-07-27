import math
ct222,l234=map(int,input().split())
mt252=[]
kt122=list(map(int,input().split()))
for j in range(0,l234):
    pt122,qt322=map(int,input().split())
    mt252.append([pt122,qt322])
for j in mt252:
    xt232=j[0]-1
    yt242=j[1]-1
    print(math.gcd(kt122[xt232],kt122[yt242]))
