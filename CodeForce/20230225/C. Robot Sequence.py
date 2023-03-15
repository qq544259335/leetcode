n = int(input())
string = input()
res = 0
for i in range(n):
    vertical, horizon = 0, 0
    for j in range(i, n):
        direction = string[j]
        if direction == 'L':
            horizon -= 1
        elif direction == 'R':
            horizon += 1
        elif direction == 'U':
            vertical += 1
        else:
            vertical -= 1
        if vertical == 0 and horizon == 0:
            res += 1
print(res)
