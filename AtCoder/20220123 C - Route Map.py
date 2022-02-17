# https://atcoder.jp/contests/abc236/tasks/abc236_c
n, m = map(int, input().split())
S = input().split()
T = input().split()
pointer = 0
for i in range(n):
    if S[i] == T[pointer]:
        pointer += 1
        print("Yes")
    else:
        print("No")