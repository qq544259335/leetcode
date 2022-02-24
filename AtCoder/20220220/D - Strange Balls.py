n = int(input())
nums = list(map(int, input().split()))
cur = ""
pile = 0
pile_up = []
for ball in nums:
    if ball == cur:
        pile += 1
        pile_up.append(ball)
        if pile == ball:
            for _ in range(ball):
                pile_up.pop(-1)
            cur = pile_up[-1] if len(pile_up) != 0 else ""
            pile = 0
            for i in range(len(pile_up )- 1, -1, - 1):
                if pile_up[i] == cur:
                    pile += 1
                else:
                    break
            print("new", pile, cur)
        print(len(pile_up))
    else:
        cur = ball
        pile = 1
        pile_up.append(ball)
        print(len(pile_up))
    print(pile_up)