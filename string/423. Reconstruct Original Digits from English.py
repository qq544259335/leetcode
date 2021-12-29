class Solution:
    def originalDigits(self, s: str) -> str:
        char_count = [0] * 26
        number_count = [0] * 10
        res = ""
        for c in s:
            char_count[ord(c) - ord('a')] += 1
        number_count[0] = char_count[ord('z') - ord('a')]
        number_count[2] = char_count[ord('w') - ord('a')]
        number_count[6] = char_count[ord('x') - ord('a')]
        number_count[8] = char_count[ord('g') - ord('a')]
        number_count[3] = char_count[ord('t') - ord('a')] - number_count[2] - number_count[8]
        number_count[4] = char_count[ord('u') - ord('a')]
        number_count[5] = char_count[ord('f') - ord('a')]- number_count[4]
        number_count[1] = char_count[ord('o') - ord('a')] - number_count[0] - number_count[2] - number_count[4]
        number_count[7] = char_count[ord('s') - ord('a')] - number_count[6]
        number_count[9] = (char_count[ord('n') - ord('a')] - number_count[1] - number_count[7]) // 2
        for i in range(0, 10):
            res += str(i) * number_count[i]
        return res


test = Solution()
s = "zeroonetwothreefourfivesixseveneightnine"
print(test.originalDigits(s))
