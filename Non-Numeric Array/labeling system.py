class Solution:
    def labelingSystem(self, string: str, limit: int) -> str:
        freq = [0] * 26
        for char in string:
            freq[ord(char) - ord('a')] += 1
        res = ""
        toBeSelected = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i] != 0:
                toBeSelected.append([i, freq[i]])
        for char, freq in toBeSelected:
            count = 0
            for i in range(len(res)):
                if freq == 0:
                    continue
                if res[i] == '?':
                    res = res[:i] + chr(ord('a') + char) + res[i + 1:]
                    freq -= 1
            while freq != 0:
                if count + 1 > limit:
                    res += "?"
                    count = 0
                else:
                    res += chr(ord('a') + char)
                    count += 1
                    freq -= 1
        if '?' in res:
            return ""
        return res


sol = Solution()
string = "bbddbbbbaa"
limit = 2
print(sol.labelingSystem(string, limit))
