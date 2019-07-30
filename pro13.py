mt1,rt1 = input().split()
mt1,rt1 = int(mt), int(rt1)
Lt11 = [ int(x) for x in input().split()]
for i in range(0,rt1) :
    at11,bt11 = input().split()
    at11,bt11 = int(at11), int(bt11)
for i in range(0,rt1):
    print(min(Lt11[at11-1:bt11]))
