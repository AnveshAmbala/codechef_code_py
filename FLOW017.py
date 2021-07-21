T = int(input())
for tc in range(T):
    (a, b, c) = map(int, input().split(' '))
    arr = [a,b,c]
    arr.sort()
    print(arr[1])