n, t = list(map(int,input().split()))
books = list(map(int,input().split()))
i = 0
j = 0
res = 0
total_time = 0
while j < n:
    total_time += books[j]
    if total_time > t:
        res = max(res, j - 1 - i + 1)
        total_time -= books[i]
        i += 1
    j += 1
print(res if total_time > t else max(res, j - 1 - i + 1))
