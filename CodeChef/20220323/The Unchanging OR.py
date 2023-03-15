import math
for _ in range(int(input())):
    n = int(input())
    log = int(math.log2(n))
    print(n - 1 - log)