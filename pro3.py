import sys, string, math
st11,st21 = input().split()
nt11 = len(st11)
nt21 = len(st21)
if nt21 > nt11 :
    i = 0
    while i<nt11 and st11[i] == st21[i] :
        i += 1
    print(nt21-i)
elif nt21 == nt11 :
    i = 0
    while i<nt21 and st11[i] == st21[i] :
        i += 1
    print(nt21-i)
else :

    i = 0
    while i<nt21 and st11[i] == st21[i] :
        i += 1
    st311 = st11[i:]
    st321 = st21[i:]
    Lt1 = list(st311)
    kt1 = 0
    for ct1 in st321 :
        if ct1 in Lt1 :
            kt1 += 1
            Lt1.remove(ct1)
    print(nt11-i-kt1)
