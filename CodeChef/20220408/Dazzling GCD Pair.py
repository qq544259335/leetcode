
for _ in range(int(input())):
    def factors(x):
        for i in range(2, x + 1):
            if x % i == 0:
                return i

    a, b = list(map(int,input().split()))
    i = float('inf')
    j = float('inf')
    end = False
    for n in range(a, b // 2 + 1):
        if n == 1:
            continue
        f= factors(n)
        if f + n <= b and i + j > f + n + n:
            i = n
            j = f + n
    if i + j == float('inf'):
        print(-1)
    else:
        print(i,j)