n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(m):
    cur = b[i]
    if cur not in a:
        print("No")
        exit()
    else:
        a.remove(cur)
print("Yes")