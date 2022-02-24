import math

for _ in range(int(input())):
    b, c = list(map(int, input().split()))
    gcd = math.gcd(b, c)
    print(c // gcd)
