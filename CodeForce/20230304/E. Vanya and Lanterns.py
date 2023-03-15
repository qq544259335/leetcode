n, l = list(map(int, input().split()))
lanterns = list(map(int, input().split()))
lanterns.sort()
max_darkness = max(lanterns[0] * 2, (l - lanterns[-1]) * 2)
for i in range(len(lanterns) - 1):
    max_darkness = max(lanterns[i + 1] - lanterns[i], max_darkness)
print('%.10f' % (max_darkness / 2))
