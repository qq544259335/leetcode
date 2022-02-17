s = input()
if len(s) == 0 or len(s) == 1:
    print('Yes')
    exit()


def check():
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


if check():
    print('Yes')
    exit()
i = len(s) - 1
count = 0
while s[i] == 'a':
    count += 1
    i -= 1
    if i == -1:
        print('Yes')
        exit()
s = s[:i + 1]
i = 0
while s[i] == 'a':
    i += 1
    count -= 1
    if count == -1:
        print('No')
        exit()
s = s[i:]
if check():
    print('Yes')
else:
    print('No')
