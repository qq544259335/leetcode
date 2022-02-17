# https://atcoder.jp/contests/abc238/tasks/abc238_c'

n = input()
digits = len(n)
print(digits)
# if digits == 0:
#     print(int(0.5 * n * (1 + n)))
#     exit()
bases = [0] * digits
for i in range(1, digits):
    bases[i] = bases[i - 1] * 10 + (10 ** i) * 45
n = n[::-1]
for i in range(digits):
