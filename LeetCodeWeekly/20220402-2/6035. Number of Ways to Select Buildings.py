class Solution:
    def numberOfWays(self, s: str) -> int:
        s = list(s)
        s_count = []
        count_same = 0
        prev = -1
        for i in range(len(s)):
            if i == 0:
                count_same = 1
                prev = s[i]

            else:
                if s[i] == prev:
                    count_same += 1
                else:
                    s_count.append(count_same)
                    count_same = 1
                    prev = s[i]
            if i == len(s) - 1:
                s_count.append(count_same)
        print(s_count)
        if len(s_count) < 3:
            return 0
        res = 0
        for i in range(len(s_count) - 2):
            j = i + 1
            while j < len(s_count):
                k = j + 1
                while k < len(s_count):
                    res += s_count[i] * s_count[j] * s_count[k]
                    print(i, j, k)
                    k += 2
                j += 2
        return res
