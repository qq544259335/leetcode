# https://atcoder.jp/contests/abc236/tasks/abc236_b
N = int(input())
cards = map(int, input().split())
count = [0] * N
for num in cards:
    count[num - 1] += 1
for i in range(len(count)):
    if count[i] != 4:
        print(i + 1)