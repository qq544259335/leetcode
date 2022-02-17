# https://www.codechef.com/START24C/problems/AVOIDCONTACT

for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    x = x - y
    if x == 0:
        print(y * 2 - 1)
    else:
        print(y * 2 + x)
