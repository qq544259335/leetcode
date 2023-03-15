for _ in range(int(input())):
    n = int(input())
    if n % 5 != 0:
        print(-1)
    else:
        res = n // 5
        if res % 2 == 0:
            print(res // 2)
        else:
            print(res // 2 + 1)
