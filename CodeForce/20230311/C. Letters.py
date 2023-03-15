n, m = list(map(int, input().split()))
dorms = list(map(int, input().split()))
if n > 1:
    for i in range(1, len(dorms)):
        dorms[i] += dorms[i - 1]
letters = list(map(int, input().split()))
dorm_num = 0
for letter in letters:
    while letter > dorms[dorm_num]:
        dorm_num += 1
    print(dorm_num + 1, letter if dorm_num == 0 else letter - dorms[dorm_num - 1])
