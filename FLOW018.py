# cook your dish here
t =  int(input())
for i in range(t):
    n = int(input())
    k =1
    while n != 0:
        k *= n
        n = n - 1
    print(k) 