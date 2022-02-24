for _ in range(int(input())):
    length = int(input())
    s = input()
    check_s = set()
    if s[:-1] not in check_s:
        check_s.add(s[:-1])
    print(check_s)
    for i in range(length - 1):
        temp = s[:i] + s[i + 1:]
        if temp not in check_s:
            check_s.add(temp)
    print(len(check_s))