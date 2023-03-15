for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    d = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if s[i] == d[i]:
            count += 1
    print(count)