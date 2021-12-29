class Solution:
    def expressiveWords(self, s: str, words: [str]) -> int:
        res = 0
        for word in words:
            if len(s) < len(word):
                continue
            match = True
            dup = 0
            i = 0
            j = 0
            cur_char = ""
            while i < len(word):
                if cur_char == word[i]:
                    dup += 1
                else:
                    if cur_char != "":
                        s_dup = 0
                        while j < len(s):
                            if s[j] == cur_char:
                                s_dup += 1
                            else:
                                break
                            j += 1
                        print(i, j, s_dup, dup, cur_char)
                        if not (s_dup == dup or s_dup >= dup + 2):
                            match = False
                    dup = 1
                    cur_char = word[i]
                i += 1
            s_dup = 0
            while j < len(s):
                if s[j] == cur_char:
                    s_dup += 1
                else:
                    break
                j += 1
            print(i, j, s_dup, dup, cur_char)
            if not (s_dup == dup or s_dup >= dup + 2):
                match = False
            print(len(s), j)
            if len(s) == j:
                res = res + 1 if match else res
        return res

test = Solution()
s = "abcd"
words = ["abc"]
print(test.expressiveWords(s, words))