for _ in range(int(input())):
    n, x = list(map(int,input().split()))
    if 3* n < x:
        print("NO")
    elif 3*n == x:
        print("YES")
        print(n,0,0)
    else:
        flag = False
        for a in range(n):
            b = 3 * a - x
            if b >= 0 and a + b <= n and 3*a - b == x:
                print("YES")
                print(a,b,n -a -b)
                flag = True
                break
        if not flag:
            print("NO")