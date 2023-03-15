abc = list(map(int,input().split()))
x = abc.pop(-1)
if x in abc:
    print("YES")
else:
    print("NO")
