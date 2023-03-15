for _ in range(int(input())):
    x, y =  list(map(int,input().split()))
    m = y // x if y % x != 0 else y // x - 1
    print(m)