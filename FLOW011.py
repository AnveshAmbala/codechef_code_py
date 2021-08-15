# cook your dish here
for i in range(int(input())):
    n = int(input())
    if n >= 1500 :
        hra = (n * (98/100))
        da = 500
        
    else:
        hra = (n * (10/100))
        da = (n * (90/100))
    print(n+hra+da)