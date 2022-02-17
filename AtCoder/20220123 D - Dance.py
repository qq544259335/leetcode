# https://atcoder.jp/contests/abc236/tasks/abc236_d

def solution():
    n = 2 * int(input())
    A = []
    for i in range(n - 1):
        A.append(list(map(int, input().split())))
    people = [i for i in range(n)]
    res = 0
    pair = []
    visited = set()

    def backtrack(temp):
        nonlocal res
        if len(people) == 0:
            res = max(res, temp)
            return
        length = len(people)
        for i in range(1, length):
            p2 = people.pop(i)
            p1 = people.pop(0)
            pair.append((p1, p2))
            temp = temp ^ A[p1][p2 - p1 - 1]
            backtrack(temp)
            people.insert(0, p1)
            people.insert(i, p2)
            pair.pop(-1)

    # def backtrack():
    #     nonlocal res
    #     print(visited, pair)
    #     if len(visited) == n:
    #         temp = 0
    #         print(pair)
    #         for p1, p2 in pair:
    #             temp = temp ^ A[p1][p2 - p1 - 1]
    #         res = max(res, temp)
    #         return
    #     p1 = -1
    #     for i in range(n):
    #         if i not in visited:
    #             p1 = i
    #             visited.add(p1)
    #             print(p1, visited)
    #             break
    #     if p1 == -1:
    #         print(visited, pair, 10001341234)
    #     for i in range(n):
    #
    #         if i in visited:
    #             continue
    #         p2 = i
    #         visited.add(p2)
    #         pair.append((p1, p2))
    #         print(visited, pair, p1, p2)
    #         backtrack()
    #         visited.remove(p2)
    #         pair.pop(-1)
    #     visited.remove(p1)

    backtrack(0)
    print(res)


solution()
