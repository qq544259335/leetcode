class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        track = []
        track_set = set()
        res = []
        def backtrack(num):
            if num == len(nums):
                res.append(track[:])
                return
            for dir in nums:
                if dir not in track_set:
                    track_set.add(dir)
                    track.append(dir)
                    backtrack( num + 1)
                    track.pop(-1)
                    track_set.remove(dir)
        backtrack(0)
        return res