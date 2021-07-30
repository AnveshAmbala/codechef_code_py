# cook your dish here
t = int(input())
l = [100, 50, 10, 5, 2, 1]
for i in range(t):
    n = int(input())
    count = 0
    for i in l:
        a = n//i
        n = n - (a*i)
        count += a
    print(count)
        
        
        