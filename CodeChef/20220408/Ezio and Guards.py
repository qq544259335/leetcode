for _ in range(int(input())):
    x, y = list(map(int,input().split()))
    if x >= y:
        print("Yes")
    else:
        print("No")