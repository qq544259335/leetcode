for _ in range(int(input())):
    n = int(input())
    base = 1
    while 2 * base <= n - 1:
        base *= 2
    res = []
    for i in range(n - 1, 0, -1):
        res.append(str(i))
        if i == base:
            res.append('0')
    print(" ".join(res))
