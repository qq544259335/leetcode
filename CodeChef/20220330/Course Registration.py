for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    if n <= m - k:
        print("Yes")
    else:
        print("No")
