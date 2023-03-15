for _ in range(int(input())):
    n, x = list(map(int,input().split()))
    left = n % 3
    res = x * left + n // 3 * x * 2
    print(res)