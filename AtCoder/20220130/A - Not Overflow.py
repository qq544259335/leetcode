# https://atcoder.jp/contests/abc237/tasks/abc237_a
num = int(input())
if -2**31 <= num <= 2**31 - 1:
    print('Yes')
else:
    print('No')