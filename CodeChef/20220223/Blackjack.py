for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a + b < 11:
        print(-1)
    elif a + b > 20:
        print(-1)
    else:
        print(21 - a - b)
