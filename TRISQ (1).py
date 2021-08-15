# cook your dish here
for i in range(int(input())):
    b = int(input())
    b -= 2
    b //= 2
    print( int(b*(b+1)//2))