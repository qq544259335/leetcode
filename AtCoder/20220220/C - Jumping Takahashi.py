n, x = list(map(int, input().split()))
a, b = [], []
for _ in range(n):
    aa, bb = list(map(int, input().split()))
    a.append(aa)
    b.append(bb)


def backtrack(nn, summ):
    print(nn, summ)
    if summ > x:
        return
    if n == nn:
        if summ != x:
            return
        else:
            print("Yes")
            exit()
    for nnn in (a[nn], b[nn]):
        backtrack(nn + 1, summ + nnn)


backtrack(0, 0)
print("No")
