class Solution:
    def prefixCount(self, words: [str], pref: str) -> int:
        count = 0
        for word in words:
            match = 0
            if len(pref) > len(word):
                continue
            for i in range(len(pref)):
                if word[i] == pref[i]:
                    match += 1
            if match == len(pref):
                count += 1
        return count