for _ in range(int(input())):
    a, b, x, y = list(map(int, input().split()))
    if x * y >= a * b:
        print("Yes")
    else:
        print("No")
