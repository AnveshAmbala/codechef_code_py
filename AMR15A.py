# cook your dish here
n = int(input())
l = input().split()
ecount = 0
ocount = 0
for i in l:
    if int(i) % 2 == 0:
        ecount += 1
    else:
        ocount += 1
if ecount > ocount:
    print("READY FOR BATTLE")
else:
    print("NOT READY")