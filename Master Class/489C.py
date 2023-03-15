# https://codeforces.com/problemset/problem/489/C
m, s = list(map(int, input().split()))
if (m == 1 and not (0 <= s <= 9)) or m > 1 and not (1 <= s <= 9 * m):
    print(-1, - 1)
else:
    count = s
    digit = m - 1
    biggest = 0
    while digit >= 0:
        biggest = biggest + 9 * 10 ** digit if count >= 9 else biggest + count * 10 ** digit
        count = max(0, count - 9)
        digit -= 1
        
    count = s - 1
    digit = 0
    smallest = 1 * 10 ** (m - 1)
    while digit < m:
        smallest = smallest + 9 * 10 ** digit if count >= 9 else smallest + count * 10 ** digit
        count = max(0, count - 9)
        digit += 1
    print(smallest, biggest)
