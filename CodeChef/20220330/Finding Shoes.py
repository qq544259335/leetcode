for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    print(n + max(0, n - m))
