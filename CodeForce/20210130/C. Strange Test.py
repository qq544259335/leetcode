for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    base_b = 1
    while 2 * base_b <= b:
        base_b *= 2

    print(min(b - a, (b | a) - b + 1, abs((b - base_b) - a) + 1))
