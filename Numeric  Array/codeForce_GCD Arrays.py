import math
for t in range(int(input())):
    minn, maxn, time = map(int, input().split())
    arr = []
    for i in range(maxn - minn + 1):
        arr.append(minn + i)
    res = 0
    for i in range(len(arr)):
        if i == 0:
            res = arr[i]
        else:
            res = math.gcd(res, arr[i])
    if res > 1:
        print("YES")
    else:
        print("NO")
