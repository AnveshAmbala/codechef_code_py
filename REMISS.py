# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int, input().split(" "))
    if a > b :
        print(str(a) + " " + str(a+b))
    else:
            print(str(b) + " " + str(a+b))
        