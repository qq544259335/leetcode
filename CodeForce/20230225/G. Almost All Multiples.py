for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    if n % x != 0:
        print(-1)
    else:
        res = []
        res.append(x)
        t = 2
        for i in range(2, n):
            if i == x:
                res.append(n)
            else:
                if t == x:
                    t += 1
                res.append(t)
                t += 1
        res.append(1)
        print(" ".join(map(str,res)))