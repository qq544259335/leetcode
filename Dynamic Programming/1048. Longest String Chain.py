class Solution:
    def longestStrChain(self, words: [str]) -> int:
        dp = [1] * len(words)
        words.sort(key=lambda x: len(x))
        def checkChain(word1, word2) -> bool:
            if len(word1) + 1 != len(word2):
                return False
            j = 0
            i = 0
            while i < len(word1) and j<len(word2):
                if word1[i] == word2[j]:
                    i += 1
                j += 1
            return i == len(word1)

        for i in range(len(words)):
            for j in range(i):
                if checkChain(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)