for i in range(int(input())):
    l = int(input())
    s = input()
    if len(s) > 2:
        print("NO")
        continue
    else:
        count = [0, 0]
        for c in s:
            count[int(c)] += 1
        if count[0] <= 1 and count[1] <= 1:
            print("YES")
        else:
            print("NO")
