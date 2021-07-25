import collections


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:  # nklogk
        resDict = collections.defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            resDict[ss].append(s)
        return list(resDict.values())

    def groupAnagramsFaster(self, strs: [str]) -> [
        [str]]:  # n(k + 26) it seems that lc testcase are all wiz some k, some the first one is quicker
        resDict = collections.defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            resDict[tuple(freq)].append(s)
        return list(resDict.values())


sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagramsFaster(strs))
