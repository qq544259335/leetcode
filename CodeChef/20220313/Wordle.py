for _ in range(int(input())):
    a = input()
    b = input()
    res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            res += "G"
        else:
            res += "B"
    print(res)