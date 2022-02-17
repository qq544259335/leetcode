# https://atcoder.jp/contests/abc238/tasks/abc238_b

length = int(input())
cuts = list(map(int, input().split()))
for i in range(1, length):
    cuts[i] = (cuts[i - 1] + cuts[i]) % 360
cuts.sort()
res = 0
for i in range(length):
    if i == 0:
        res = max(res, cuts[0])
    else:
        res = max(res, cuts[i] - cuts[i - 1])
res = max(res, 360 - cuts[-1])
print(res)
