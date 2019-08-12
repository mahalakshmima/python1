import sys,string


def maxOfSegmentMins(Lact1, nect1, kint1):
    if kint1 == 1:
        return min(Lact1)
    if kint1 == 2 :
        return max(Lact1[0], Lact1[nect1 - 1])
    return max(Lact1)

nect1,kint1 = input().split()
nect1,kint1 = int(nect1),int(kint1)
Lact1 = [ int(x) for x in input().split()]
nect1 = len(Lact1)
ans1 = maxOfSegmentMins(Lact1, nect1, kint1)
print(ans1)
