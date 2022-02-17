for _ in range(int(input())):
    n, num = list(map(int, input().split()))
    print(num % (n + 1))
