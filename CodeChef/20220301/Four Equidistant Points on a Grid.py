n = int(input())
if n % 2 == 1:
    print(-1)
else:
    print("0 0")
    print(str(0) + " " + str(-n))
    print(str(n // 2) + " " + str(-n // 2))
    print(str(-n // 2) + " " + str(-n // 2))
