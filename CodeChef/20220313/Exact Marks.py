for _ in range(int(input())):
    n, x = list(map(int,input().split()))
    if 3* n < x:
        print("NO")
    elif 3*n == x:
        print("YES")
        print(n,0,0)
    else:
        end = (n + x)//4 + 1
        start = x // 3 +1
        flag = False
        for a in (start,end):
            b = 3 * a - x
            if a + b <= n:
                print("YES")
                print(a,b,n -a -b)
                flag = True
                break
        if not flag:
            print("NO")