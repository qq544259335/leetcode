for _ in range(int(input())):
    x,y,n = list(map(int,input().split()))
    if abs(x - y) <= n:
        print("YES")
    else:
        print("NO")