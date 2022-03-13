for _ in range(int(input())):
    n = int(input())
    n -= 1
    if (n % 7) >= 5:
        print(n//7 + 1)
    else:
        print(n//7)