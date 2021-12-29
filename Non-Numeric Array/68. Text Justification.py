class Solution:
    def fullJustify(self, words: [str], maxWidth: int) -> [str]:
        res = []
        pivot = 0
        last = False
        while pivot < len(words):
            cur_space = maxWidth
            temp_res = []
            first_word = True
            while pivot < len(words):
                length = len(words[pivot]) + 1
                if first_word:
                    first_word = False
                    length -= 1
                if length > cur_space:
                    break
                else:
                    cur_space -= length
                    temp_res.append(words[pivot])
                    pivot += 1
                    if pivot == len(words):
                        last = True
            if not last:
                if len(temp_res) == 1:
                    temp_res[0] += (maxWidth - len(temp_res[0])) * ' '
                    res.append(temp_res[0])
                else:
                    times = cur_space // (len(temp_res) - 1)
                    left = cur_space % (len(temp_res) - 1)
                    print(cur_space, times, left)
                    p = 0
                    for _ in range(left):
                        temp_res[p] += ' '
                        p += 1
                    padding = (times + 1) * ' '
                    res.append(padding.join(temp_res))
            else:
                temp_str = ' '.join(temp_res)
                temp_str += (maxWidth - len(temp_str)) * ' '
                res.append(temp_str)
        return res


sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(sol.fullJustify(words, maxWidth))
