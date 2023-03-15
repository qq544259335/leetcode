import heapq
for _ in range(int(input())):
    n, coins = list(map(int, input().split()))
    teleporters = list(map(int, input().split()))
    heap = []
    for i in range(n):
        teleporters[i] += i + 1
        heapq.heappush(heap, teleporters[i])
    res = 0
    while coins > 0 and heap:
        cost = heapq.heappop(heap)
        if cost <= coins:
            coins -= cost
            res += 1
        else:
            break
    print(res)