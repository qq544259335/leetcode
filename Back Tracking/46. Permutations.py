class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        res = []
        track = []
        used = [0] * len(nums)

        def backtrack():
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    track.append(nums[i])
                    used[i] = 1
                    backtrack()
                    used[i] = 0
                    track.pop(-1)
            return

        backtrack()
        return res
