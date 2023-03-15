class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        falling_r = False
        start = 0
        res = ""
        for i in range(len(dominoes)):
            if dominoes[i] == 'L':
                if not falling_r:
                    res += (i - start + 1) * "L"
                else:
                    res += (i - start + 1) // 2 * "R"
                    if (i - start + 1) % 2 == 1:
                        res += '.'
                    res += (i - start + 1) // 2 * "L"
                start = i + 1
                falling_r = False
            if dominoes[i] == 'R':
                res += (i - start) * 'R' if falling_r else (i - start) * '.'
                start = i
                falling_r = True
        if len(res) != len(dominoes):
            res += (len(dominoes) - len(res)) * 'R' if falling_r else (len(dominoes) - len(res)) * '.'
        return res
