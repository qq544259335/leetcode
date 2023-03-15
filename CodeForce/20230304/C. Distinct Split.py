for _ in range(int(input())):
    _ = input()
    string = input()
    set_a = [0] *26
    count_a = 0
    set_b = [0] * 26
    count_b = 0
    for c in string:
        set_b[ord(c) - ord('a')] += 1
        if set_b[ord(c) - ord('a')] == 1:
            count_b += 1
    res = -1
    for i in range(len(string) - 1):
        set_b[ord(string[i]) - ord('a')] -= 1
        set_a[ord(string[i]) - ord('a')] += 1
        if set_b[ord(string[i]) - ord('a')] == 0:
            count_b -= 1
        if set_a[ord(string[i]) - ord('a')] == 1:
            count_a += 1
        res = max(res, count_b + count_a)
    print(res)
