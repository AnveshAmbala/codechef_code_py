# cook your dish here
import math
t  = int(input())
for i in range(t):
    a, b = map(int,input().split(" "))
    g = 0
    if ( a > b):
        g = a
    else:
        g = b
    while(True):
        
        if((g % a == 0) and (g % b == 0)):
            lcm = g
            break
        g += 1
    print(math.gcd(a,b), lcm)
  
    
    
    
