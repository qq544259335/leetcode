for _ in range(int(input())):
    n = int(input())
    seqs = list(map(int, input().split()))
    seqs.insert(0, - 1)
    valid = [0] * (n + 1)
    valid[0] = 1
    for i in range(1, n + 1):
        if seqs[i] + i <= n:
            valid[i + seqs[i]] |= valid[i - 1]
        if i - 1 - seqs[i] >= 0:
            valid[i] |= valid[i - 1 - seqs[i]]
    print("YES") if valid[-1] else print("No")
