for _ in range(int(input())):
    abcd = list(map(int,input().split()))
    a,b,c,d = abcd[0],abcd[1],abcd[2],abcd[3]
    count = 0
    if a not in [c,d]:
        count += 1
    if b not in [c,d]:
        count += 1
    print(count)