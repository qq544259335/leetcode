class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        temp = []
        for n in text:
            if n == pattern[0]:
                temp.append(n)
            elif n == pattern[1]:
                temp.append(n)
        res = 0
        if pattern[0] != pattern[1]:
            temp_str = "".join(temp)
            temp_strs = [temp_str + pattern[1], pattern[0] + temp_str]
            for t in temp_strs:
                total_count = 0
                count1 = 0
                for n in t:
                    if n == pattern[0]:
                        count1 += 1
                    else:
                        total_count += count1
                res = max(res, total_count)
            return res
        else:
            length = len(temp) + 1
            return (length - 1) * length // 2
