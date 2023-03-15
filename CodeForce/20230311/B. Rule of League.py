for _ in range(int(input())):
    n, x, y = list(map(int, input().split()))
    if x * y != 0 or (x == 0 and y == 0):
        print(-1)
    else:
        if y != 0:
            x, y = y, x
        if (n - 1) % x != 0:
            print(-1)
        else:
            res = ""
            for i in range((n - 1) // x):
                if i == 0:
                    res += "1 " * x
                else:
                    res += (str(2 + i * x) + " ") * x
            print(res)
