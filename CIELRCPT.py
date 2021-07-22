x=int(input())
for i in range(x):
    y=int(input())
    ans=0
    list=[2048,1024,512,256,128,64,32,16,8,4,2,1]
    while y>0:
        for j in list:
            if y>=j:
                ans+=y//j
                y%=j
    print(ans)  
