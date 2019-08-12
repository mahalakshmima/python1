import sys, string, math

samt1 = input()
if samt1 == samt1[::-1] :
    print('yes')
    sys.exit()
kimt1 = 0
for cust in samt1[::-1] :
    if cust == '0' :
        kimt1 += 1
    else :
        break
sopt1 = '0'*kimt1 + samt1

if sopt1 == sopt1[::-1] :
    print('yes')
else :
    print('no')
