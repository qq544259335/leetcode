for _ in range(int(input())):
    n, x, y = list(map(int, input().split()))
    s = input()
    count = [0 , 0]
    for c in s:
        count[int(c)] += 1
    if count[0] == 0 or count[1] == 0:
        print(0)
    else:
        print(min(x,y))